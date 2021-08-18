class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        count = collections.Counter(nums)

        for n in nums:

            if count[n] != 0:

                for v in range(n, n + k):
                    count[v] -= 1
                    if count[v] < 0:
                        return False

        return True
