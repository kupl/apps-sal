class Solution:

    def isPossibleDivide(self, nums, k):
        if len(nums) % k:
            return False
        Ct = Counter(nums)
        heapify(nums)
        while Ct:
            num = heappop(nums)
            while not Ct[num]:
                num = heappop(nums)
            for i in range(k):
                if not Ct[num + i]:
                    return False
                if Ct[num + i] == 1:
                    del Ct[num + i]
                else:
                    Ct[num + i] -= 1
        return True
