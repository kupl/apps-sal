class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        sortedNums = sorted(nums)
        counts = collections.Counter(nums)

        for num in sortedNums:
            if counts[num] == 0:
                continue

            counts[num] -= 1
            for i in range(1, k):
                if num + i not in counts:
                    return False

                if counts[num + i] == 0:
                    return False

                counts[num + i] -= 1

        return True
