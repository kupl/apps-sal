import sys


class DRecoverIt:

    def gd(selfs, x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return x // i

    def sieve(self, prime):
        for i in range(2, int(len(prime) ** 0.5) + 1):
            if not prime[i]:
                continue
            m = 2
            while m * i < len(prime):
                prime[m * i] = False
                m += 1
        return prime

    def solve(self):
        is_prime = [True] * 2750135
        is_prime[0] = False
        is_prime[1] = False
        self.sieve(is_prime)
        p = [-1]
        for i in range(len(is_prime)):
            if is_prime[i]:
                p.append(i)
        n = int(input())
        b = [int(item) for item in input().split()]
        b.sort(reverse=True)
        cnt = {x: 0 for x in b}
        for x in b:
            cnt[x] += 1
        p_order = {}
        for i in range(1, len(p)):
            p_order[p[i]] = i
        res = []
        for i in range(2 * n):
            if cnt[b[i]] == 0:
                continue
            if is_prime[b[i]]:
                if b[i] < len(p) and p[b[i]] in cnt and (cnt[p[b[i]]] > 0):
                    res.append(b[i])
                    cnt[p[b[i]]] -= 1
                    cnt[b[i]] -= 1
                elif p_order[b[i]] in cnt and cnt[p_order[b[i]]] > 0:
                    res.append(p_order[b[i]])
                    cnt[p_order[b[i]]] -= 1
                    cnt[b[i]] -= 1
            else:
                d = self.gd(b[i])
                assert d in cnt
                res.append(b[i])
                cnt[b[i]] -= 1
                cnt[d] -= 1
        print(*res)


solver = DRecoverIt()
input = sys.stdin.readline
solver.solve()
