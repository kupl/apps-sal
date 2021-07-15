from heapq import heappop, heappush

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        es_list = [[-e, s] for s, e in zip(speed, efficiency)]
        es_list.sort()
        
        queue = []
        
        total_speed = 0
        cur_eff = 0
        res = 0
        for e, s in es_list:
            #print(e, s, queue, total_speed, res)
            if -e < cur_eff:
                res = max(res, cur_eff * total_speed)

            if len(queue) == k:
                if not queue or queue[0] < s:
                    pre_s = heappop(queue)
                    total_speed -= pre_s
            if not queue or len(queue) < k:
                heappush(queue, s)
                total_speed += s
                cur_eff = -e
        return max(res, total_speed*cur_eff)%(10**9 + 7)
            
            

