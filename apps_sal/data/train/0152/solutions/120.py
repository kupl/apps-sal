class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(arr, n, m, mid):
            magnet = 1
            pos = arr[0]
            for i in range(1, n):
                if arr[i] - pos >= mid:
                    magnet += 1
                    pos = arr[i]
                    if magnet == m:
                        return 1
            return 0
        position.sort()
        l = 0
        n = len(position)
        r = position[n - 1]
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if not check(position, n, m, mid):
                r = mid - 1
            else:
                res = max(res, mid)
                l = mid + 1
        return res
