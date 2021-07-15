class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        left_pos = 0
        left_neg = sys.maxsize
        ans = 0
        cp = 1
        for i, num in enumerate(nums):
            if num == 0:
                cp = 1
                left_pos = i + 1
                left_neg = sys.maxsize
            else:
                cp *= num
                # print(\"haha\", cp)
                if cp > 0:
                    ans = max(ans, i - left_pos + 1)
                    # print(\"hehe\", ans, num, cp)
                else:
                    ans = max(ans, i - left_neg)
                    # print(\"hehe\", ans, num, cp, left_neg)
                
                if cp < 0 and left_neg == sys.maxsize:
                    left_neg = i
        return ans
