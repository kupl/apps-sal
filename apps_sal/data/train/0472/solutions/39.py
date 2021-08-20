class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        while len(q) > 0:
            curr_idx = q.popleft()
            if arr[curr_idx] == 0:
                return True
            for next_idx in [curr_idx + arr[curr_idx], curr_idx - arr[curr_idx]]:
                if 0 <= next_idx < len(arr):
                    if next_idx not in visited:
                        q.append(next_idx)
                        visited.add(next_idx)
        return False
