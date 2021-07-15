class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()
        while q:
            curr = q.popleft()
            if arr[curr]==0: return True
            if curr not in visited:
                visited.add(curr)
                if curr+arr[curr]<len(arr):
                    q.append(curr+arr[curr])
                if curr-arr[curr]>=0:
                    q.append(curr-arr[curr])
        return False
