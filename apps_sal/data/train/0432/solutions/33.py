class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        sortedNums = sorted(set(nums))
        counts = collections.Counter(nums)
        for num in sortedNums:
            if counts[num] == 0:
                continue
            for i in range(1, k):
                if num + i not in counts:
                    return False
                if counts[num + i] < counts[num]:
                    return False
                counts[num + i] -= counts[num]
        return True
