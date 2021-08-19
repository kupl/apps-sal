# 18:31 -
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:

        def extra_to_append(w1, w2):
            for i in range(len(w1)):
                if w2.startswith(w1[i:]):
                    return w2[len(w1) - i:]
            return w2

        n = len(A)
        extra = [[''] * n for _ in range(n)]
        for (i, j) in itertools.permutations(list(range(n)), 2):
            extra[i][j] = extra_to_append(A[i], A[j])

        dp = [[''] * n for _ in range(1 << n)]
        ret = ''
        for mask in range(1, 1 << n):
            for (ci, cw) in enumerate(A):
                if not mask & (1 << ci):
                    continue
                pre_mask = mask & (~(1 << ci))
                if not pre_mask:
                    dp[mask][ci] = cw
                else:
                    for (pi, pw) in enumerate(A):
                        if not pre_mask & (1 << pi):
                            continue
                        if not dp[mask][ci] or len(dp[mask][ci]) > len(dp[pre_mask][pi]) + len(extra[pi][ci]):
                            dp[mask][ci] = dp[pre_mask][pi] + extra[pi][ci]
                if mask == (1 << n) - 1:
                    ret = dp[mask][ci] if not ret or len(ret) > len(dp[mask][ci]) else ret

        return ret
