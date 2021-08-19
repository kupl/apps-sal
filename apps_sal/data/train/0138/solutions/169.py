class Solution:

    def calc(self, neg: List[int], i: int) -> int:
        if len(neg) % 2 == 0:
            return i
        else:
            return max(i - neg[0] - 1, neg[-1])

    def getMaxLen(self, nums: List[int]) -> int:
        ml = 0
        while True:
            neg = []
            for (idx, i) in enumerate(nums):
                if i == 0:
                    ml = max(self.calc(neg, idx), ml)
                    nums = nums[idx + 1:]
                    break
                elif i < 0:
                    neg.append(idx)
            else:
                if nums != []:
                    ml = max(ml, self.calc(neg, idx + 1))
                break
        return ml
