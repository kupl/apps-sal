class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k:
            return False
        Ct = Counter(nums)

        while Ct:
            start = min(Ct)
            for i in range(start, start + k):
                if not Ct[i]:
                    return False
                if Ct[i] == 1:
                    del Ct[i]
                else:
                    Ct[i] -= 1

        return True
