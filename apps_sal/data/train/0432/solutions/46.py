class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        c = collections.Counter(nums)
        for num in c:
            if c[num] != 0:
                for i in range(1, k):
                    if num + i in c and c[num + i] >= c[num]:
                        c[num + i] -= c[num]
                    else:
                        return False
            c[num] = 0
        return True
