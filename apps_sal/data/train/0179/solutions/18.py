def stringcomp(a, i, last, k, count, memo):
    if (i, last, k, count) in memo:
        return memo[((i, last, k, count))]
    if k < 0:
        return float('inf')
    if i >= len(a):
        return 0
    if a[i] == last:
        keepi = stringcomp(a, i + 1, last, k, count + 1, memo) + (1 if count in (1, 9, 99, 999) else 0)
        deletei = stringcomp(a, i + 1, last, k - 1, count, memo)
    else:
        keepi = 1 + stringcomp(a, i + 1, a[i], k, 1, memo)
        deletei = stringcomp(a, i + 1, last, k - 1, count, memo)
    memo[((i, last, k, count))] = min(keepi, deletei)
    return min(keepi, deletei)


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return stringcomp(s, 0, '', k, 0, {})
