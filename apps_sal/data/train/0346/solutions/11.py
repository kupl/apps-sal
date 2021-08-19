def solve(A, k):
    count = [0, 0]
    front = iter(A)
    ans = 0
    size = 0
    for v in A:
        count[v % 2] += 1
        size += 1
        while count[1] > k:
            count[next(front) % 2] -= 1
            size -= 1
        ans += size
    return ans


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return solve(nums, k) - solve(nums, k - 1)
