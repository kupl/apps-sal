def solve(A, k):
    count = [0, 0]
    lower = (x % 2 for x in A)

    ans = 0
    for x in (x % 2 for x in A):
        count[x] += 1
        while count[1] > k:
            count[next(lower)] -= 1
        ans += sum(count)

    return ans


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return solve(nums, k) - solve(nums, k - 1)
