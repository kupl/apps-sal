class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()
        N = len(arr)
        while q:
            cur = q.popleft()
            if cur in visited: continue
            visited.add(cur)
            if arr[cur] == 0: return True
            if cur + arr[cur] < N:
                q.append(cur + arr[cur])
            if cur - arr[cur] >= 0:
                q.append(cur - arr[cur])
        return False
