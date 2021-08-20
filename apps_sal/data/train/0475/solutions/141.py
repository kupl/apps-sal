class Solution:

    def rangeSum(self, nums: List[int], n: int, l: int, r: int) -> int:
        psum = [0]
        for v in nums:
            psum.append(v + psum[-1])
        psum = psum[1:]
        arr = []
        for i in range(0, n):
            for j in range(i, n):
                arr.append(psum[j] - psum[i] + nums[i])
        arr.sort()
        re = 0
        for i in range(l - 1, r):
            re = (re + arr[i]) % 1000000007
        return re
