class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
        m = collections.Counter(A)
        res = 0
        for (n0, n1) in itertools.combinations_with_replacement(m, 2):
            n2 = target - n0 - n1
            if n0 == n1 == n2:
                res += m[n0] * (m[n0] - 1) * (m[n0] - 2) // 6
            elif n0 == n1 != n2:
                res += m[n0] * (m[n0] - 1) // 2 * m[n2]
            elif max(n0, n1) < n2:
                res += m[n0] * m[n1] * m[n2]
        return res % (10 ** 9 + 7)
