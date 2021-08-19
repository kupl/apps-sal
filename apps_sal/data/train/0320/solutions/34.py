class Solution:
    # mine
    def minOperations0(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0

        def turnEven():
            nonlocal ans
            for i in range(l):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1

        def countZero():
            count = 0
            for n in nums:
                if n == 0:
                    count += 1
            return count

        while True:
            turnEven()
            if countZero() == l:
                return ans
            for i in range(l):
                nums[i] //= 2
            ans += 1

    # copied https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/discuss/805740/JavaC%2B%2BPython-Bit-Counts
    # 其实思路跟上面是一样的
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        maxLen = 1
        for n in nums:
            bits = 0
            while n > 0:
                res += n & 1
                bits += 1
                n >>= 1
            maxLen = max(maxLen, bits)
        return res + maxLen - 1
