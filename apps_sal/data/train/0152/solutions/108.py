class Solution:
    def is_valid(self, arr, force, m):
        cnt = 1
        prev = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - prev >= force:
                cnt += 1
                prev = arr[i]

            if cnt == m:
                return True

        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        res = -1

        position.sort()

        left = 1
        right = position[len(position) - 1]

        while left + 1 < right:
            mid = (right - left) // 2 + left

            if (self.is_valid(position, mid, m)):
                # Too small
                left = mid
                res = max(res, mid)
            else:
                # Too big
                right = mid

        for i in range(left, right + 1):
            if self.is_valid(position, i, m):
                res = max(res, i)

        return res
