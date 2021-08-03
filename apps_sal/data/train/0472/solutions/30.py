class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def solve(arr, i, done):
            if arr[i] == 0:
                return True
            elif i in done:
                return False
            else:
                a, b = False, False
                if 0 <= i + arr[i] < len(arr):
                    done[i] = 1
                    a = solve(arr, i + arr[i], done)
                if 0 <= i - arr[i] < len(arr):
                    done[i] = 1
                    b = solve(arr, i - arr[i], done)
                return a or b
        return solve(arr, start, {})
