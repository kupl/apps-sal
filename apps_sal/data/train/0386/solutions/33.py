class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = [1], [1], [1], [1], [1]
        mod = 10**9 + 7
        if n == 0:
            return 0
        for top, countDown in enumerate(range(n, 1, -1)):
            a.append(e[top] % mod)
            e.append((a[top] + i[top]) % mod)
            i.append((a[top] + e[top] + o[top] + u[top]) % mod)
            o.append((i[top] + u[top]) % mod)
            u.append(a[top] % mod)

        return (a[-1] + e[-1] + i[-1] + o[-1] + u[-1]) % mod
