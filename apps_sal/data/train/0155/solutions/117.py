def max_jump(a, d, memo, i):
    if i in memo:
        return memo[i]
    max_ = 0
    for j in range(1, d + 1):
        if i + j >= len(a) or a[i + j] >= a[i]:
            break
        max_ = max(max_, max_jump(a, d, memo, i + j))
    for j in range(1, d + 1):
        if i - j < 0 or a[i - j] >= a[i]:
            break
        max_ = max(max_, max_jump(a, d, memo, i - j))
    memo[i] = max_ + 1
    return max_ + 1


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}
        for i in range(len(arr)):
            max_jump(arr, d, memo, i)
        return max(memo.values())
