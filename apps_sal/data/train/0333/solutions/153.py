class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pos = {}
        for i, x in enumerate(arr):
            if x in pos:
                pos[x][0].append(i)
            else:
                pos[x] = [[i], False]
            
        q = deque([(len(arr) - 1, 0, True), (0, 0, False)])
        visited = [[-1,-1] for _ in range(len(arr))]
        
        while q:
            i, n, d = q.popleft()
            
            if visited[i][int(not d)] != -1:
                return n + visited[i][int(not d)]
            
            if visited[i][int(d)] != -1:
                continue
            visited[i][int(d)] = n
            
            if i < len(arr) - 1:
                q.append((i+1, n+1, d))
            if i > 0:
                q.append((i-1, n+1, d))
            
            if not pos[arr[i]][1]:
                for idx in pos[arr[i]][0]:
                    q.append((idx, n+1, d))
                pos[arr[i]][1] = True
