class Solution:

    def isPossibleDivide(self, nums, k: int) -> bool:
        if not nums or not k:
            return False
        c = Counter(nums)
        nums.sort()
        for num in nums:
            if num not in c:
                continue
            for i in range(k):
                if num + i in c and c[num + i] > 0:
                    c[num + i] -= 1
                    if c[num + i] == 0:
                        del c[num + i]
                else:
                    return False
        return True
