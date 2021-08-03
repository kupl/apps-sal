class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def jump(arr, start, n, g):
            g += 1
            if g > 25:
                return False
            if start < 0 or start > n - 1:
                return False

            if arr[start] == 0:
                return True

            if jump(arr, start + arr[start], n, g):
                return True
            else:
                if jump(arr, start - arr[start], n, g):
                    return True
                else:
                    return False

        return jump(arr, start, len(arr), 0)
