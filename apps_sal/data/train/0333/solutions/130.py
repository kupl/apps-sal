class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque([0])
        visited = set([0])
        map = defaultdict(list)
        
        for idx, num in enumerate(arr):
            map[num].append(idx)
            
        step = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                pos = queue.popleft()
                if pos == len(arr) - 1:
                    return step
                for nxt in [pos - 1, pos + 1]:
                    if nxt < 0 or nxt >= len(arr) or nxt in visited:
                        continue
                    queue.append(nxt)
                    visited.add(nxt)
                for neighbor in map[arr[pos]]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                #  避免TLE ,第一次已经把所有值相同的加到了queue，之后访问到和当前值相同的idx时 不需要再apply 第三条规则
                # 即for neighbor in map[arr[pos]]
                del map[arr[pos]]
            
            step += 1
        return -1

