class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def calc(num):
            tmp = 1
            ans = [0, 0]
            count = 0
            while tmp <= num:
                if (tmp & num) != 0:
                    ans[0] += 1
                count += 1
                tmp <<= 1
            ans[1] = count - 1
            return ans
        result = 0
        tt = 0
        for num in nums:
            r = calc(num)
            result += r[0]
            tt = max(tt, r[1])
        result += tt
        return result
