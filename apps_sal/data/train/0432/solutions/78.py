class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0 or len(nums) % k != 0:
            return False
        counter = collections.Counter(nums)
        while counter:
            starter = min(counter.keys())
            for i in range(k):
                if starter + i not in counter:
                    return False
                else:
                    counter[starter + i] -= 1
                    if counter[starter + i] == 0:
                        del counter[starter + i]
        return True
