class Solution:
    def minJumps(self, arr: List[int]) -> int:

        m = len(arr)
        seen = [False for _ in range(m)]
        q = deque()
        step = 0

        quick_jump_graph = {}

        for i in range(len(arr)):
            if arr[i] in quick_jump_graph:
                quick_jump_graph[arr[i]].append(i)
            else:
                quick_jump_graph[arr[i]] = [i]

        q.append(0)

        while(len(q)):
            s = len(q)
            for i in range(s):
                cur_idx = q.popleft()
                if cur_idx < 0 or cur_idx >= m or seen[cur_idx]:
                    continue
                elif cur_idx == m - 1:
                    return step
                else:
                    seen[cur_idx] = True
                    q.append(cur_idx + 1)
                    q.append(cur_idx - 1)
                    if len(quick_jump_graph[arr[cur_idx]]) != 0:
                        for num in quick_jump_graph[arr[cur_idx]]:
                            q.append(num)
                        quick_jump_graph[arr[cur_idx]] = []
            step += 1

        return -1
