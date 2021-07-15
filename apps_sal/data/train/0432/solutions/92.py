from collections import defaultdict, Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        elif not k:
            return True
        counter = Counter(nums)
        while counter:
            start, count = sorted(counter)[0], 0
            while count < k:
                if counter[start] == 0:
                    return False
                counter[start] -= 1
                if not counter[start]:
                    counter.pop(start)
                start += 1
                count += 1
        return not counter
