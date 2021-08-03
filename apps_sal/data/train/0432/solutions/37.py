from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums or not k or k > len(nums) or len(nums) % k:
            return False
        nums.sort()
        counter = Counter(nums)
        while counter:
            count = 0
            start = sorted(counter)[0]
            while count < k:
                if counter[start] == 0:
                    return False
                counter[start] -= 1
                if counter[start] == 0:
                    counter.pop(start)
                start += 1
                count += 1
        return not counter
