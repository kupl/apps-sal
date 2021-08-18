from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        for num in sorted(counter.keys()):
            count = counter[num]
            if count == 0:
                continue
            for i in range(num, num + k):
                counter[i] -= count
                if counter[i] < 0:
                    return False
        return True
