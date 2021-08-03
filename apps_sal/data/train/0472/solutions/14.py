class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr:
            return False
        if start < 0 or start >= len(arr):
            return False

        queue = collections.deque()
        queue.append(start)
        visited = set([start])
        while queue:
            curr = queue.popleft()
            if arr[curr] == 0:
                return True
            if 0 <= curr + arr[curr] < len(arr) and curr + arr[curr] not in visited:
                queue.append(curr + arr[curr])
                visited.add(curr + arr[curr])
            if 0 <= curr - arr[curr] < len(arr) and curr - arr[curr] not in visited:
                queue.append(curr - arr[curr])
                visited.add(curr - arr[curr])

        return False
