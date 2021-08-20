class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        neg = dict()
        pos = dict()
        zero = 0
        for n in A:
            if n < 0:
                if -n not in neg:
                    neg[-n] = 0
                neg[-n] += 1
            elif n > 0:
                if n not in pos:
                    pos[n] = 0
                pos[n] += 1
            else:
                zero += 1
        if zero % 2 != 0:
            return False

        def helper(nums):
            num_sorted = sorted(list(nums.keys()), reverse=True)
            while num_sorted:
                a = num_sorted.pop()
                if nums[a] == 0:
                    continue
                if 2 * a not in nums or nums[a] > nums[2 * a]:
                    return False
                nums[2 * a] -= nums[a]
            return True
        return helper(pos) and helper(neg)
