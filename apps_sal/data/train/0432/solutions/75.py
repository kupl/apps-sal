from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        d = Counter(nums)
        for x in sorted(nums):
            if x in d:
                for y in range(x, x + k):
                    if y in d:
                        d[y] -= 1
                        if d[y] == 0:
                            del d[y]
                    else:
                        return False
        return True
