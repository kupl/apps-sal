class Solution:

    def minOperations(self, nums: List[int]) -> int:
        oneCnt = 0
        pwrCnt = 0
        for num in nums:
            if num == 0:
                continue
            exp = 0
            while num > 0:
                if num % 2 == 0:
                    num /= 2
                    exp += 1
                else:
                    num -= 1
                    oneCnt += 1
            pwrCnt = max(pwrCnt, exp)
        return oneCnt + pwrCnt
