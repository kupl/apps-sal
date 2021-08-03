class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter(nums)
        for n in sorted(counter):
            num = counter[n]
            if num > 0:
                for i in range(k):
                    counter[n + i] -= num
                    if counter[n + i] < 0:
                        return False
        return True
