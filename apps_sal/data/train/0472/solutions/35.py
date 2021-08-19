class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def helper(i):
            if i in visited:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            left = helper(i - arr[i]) if i - arr[i] >= 0 else False
            right = helper(i + arr[i]) if i + arr[i] < len(arr) else False
            return left or right
        return helper(start)
