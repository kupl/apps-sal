class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        for num in sorted(c):
            if c[num] != 0:
                for i in range(1, k):
                    if num + i in c:
                        c[num + i] -= c[num]
                        if c[num + i] < 0:
                            return False
                    else:
                        return False
            c[num] = 0
        return True
