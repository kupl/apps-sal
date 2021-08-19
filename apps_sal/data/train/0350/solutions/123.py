from collections import Counter


def solve(A, K):
    count = Counter()
    front = iter(A)
    size = 0
    ans = 0
    for k in A:
        count[k] += 1
        size += 1
        while len(count) > K:
            key = next(front)
            count[key] -= 1
            size -= 1
            if count[key] == 0:
                del count[key]
        ans += size
    return ans


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return solve(A, K) - solve(A, K - 1)
