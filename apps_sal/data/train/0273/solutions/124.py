class Solution:
    def racecar(self, target: int) -> int:
        boundary = 2*target+1
        forw_stat = [target*3] * boundary
        back_stat = [target*3] * boundary
        actions = []
        _s = 1
        queue = []
        while True:
            _jump  = 2**_s - 1
            if _jump >= boundary: break
            actions.append((_jump, _s))  # jump, step
            actions.append((-_jump, _s)) 
            queue.append((_s, _jump, 1))
            forw_stat[_jump] = _s
            _s += 1
        # print(actions)
        # --
        import heapq
        heapq.heapify(queue)
        while len(queue)>0:
            step, posi, is_forw = heapq.heappop(queue)
            # --
            for _jump, _step in actions:
                if _jump * is_forw > 0:
                    next_step, next_posi, next_is_forw = (step+_step+2, posi+_jump, is_forw)
                else:
                    next_step, next_posi, next_is_forw = (step+_step+1, posi+_jump, -is_forw)
                # --
                if next_posi<0 or next_posi>=boundary: continue
                cur_stat = forw_stat if next_is_forw==1 else back_stat
                if next_step < cur_stat[next_posi]:
                    cur_stat[next_posi] = next_step
                    heapq.heappush(queue, (next_step, next_posi, next_is_forw))
        # --
        return min(forw_stat[target], back_stat[target])

