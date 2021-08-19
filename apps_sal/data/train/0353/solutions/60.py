class Solution:

    def get_val(self, arr, i, m1, m2, target):
        if i == len(arr):
            return 0
        x = m1
        y = m2
        ct = 0
        if m1 + m2 < target:
            ct += 1
        for j in range(i + 1, len(arr)):
            m1 = min(x, arr[j])
            m2 = max(y, arr[j])
            if m1 + m2 > target:
                continue
            ct += self.get_val(arr, j, m1, m2, target)
        return ct

    def get_smallest_idx(self, arr, i, j, x):
        if arr[i] > x:
            return -1
        l = i
        h = j
        while l <= h:
            mid = int((l + h) / 2)
            if arr[mid] > x:
                h = mid - 1
            elif mid == h or arr[mid + 1] > x:
                return mid
            else:
                l = mid + 1

    def numSubseq(self, nums: List[int], target: int) -> int:
        """ct = 0
        for i in range(len(nums)):
            m1 = nums[i]
            m2 = nums[i]
            ct += self.get_val(nums,i,m1,m2,target)
        return ct%(10**9+7)"""
        nums.sort()
        ct = 0
        N = len(nums)
        j = N - 1
        s = [1 for i in range(N)]
        for i in range(1, N):
            s[i] = 2 * s[i - 1]
        for i in range(N):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            if j < i:
                return ct % (10 ** 9 + 7)
            ct += s[j - i]
        return ct % (10 ** 9 + 7)
