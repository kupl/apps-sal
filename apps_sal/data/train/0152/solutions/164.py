class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        res = -1

        left = position[0]
        right = position[n - 1]
        while left < right:
            mid = (left + right) // 2
            if self.isFeasible(position, mid, m):
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid

        if res == -1:
            left = 0
            right = position[0]
            while left < right:
                mid = (left + right) // 2
                if self.isFeasible(position, mid, m):
                    res = max(res, mid)
                    left = mid + 1
                else:
                    right = mid

        return res

    def isFeasible(self, arr, mid, m):
        n = len(arr)
        pos = arr[0]
        count = 1
        for i in range(1, n):
            if arr[i] - pos >= mid:
                pos = arr[i]
                count += 1
                if count == m:
                    return True
        return False
