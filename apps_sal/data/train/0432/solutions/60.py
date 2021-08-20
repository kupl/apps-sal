class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        counts = Counter(nums)
        for num in sorted(counts):
            prev = num
            frequency = counts[num]
            if counts[num] > 0:
                for i in range(1, k):
                    nextNum = prev + 1
                    if nextNum not in counts:
                        return False
                    elif counts[nextNum] - frequency < 0:
                        return False
                    counts[nextNum] -= frequency
                    prev = nextNum
                counts[num] -= frequency
        return True
