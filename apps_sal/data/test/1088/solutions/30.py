N, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in [0] * N]
MOD = 998244353
B = [[A[j][i] for j in range(N)] for i in range(N)]


def f(A):
    import sys
    sys.setrecursionlimit(10**7)

    class UnionFind:
        def __init__(self, N):
            self.Parent = list(range(N))
            self.size = [1] * N

        def get_Parent(self, n):
            if self.Parent[n] == n:
                return n
            p = self.get_Parent(self.Parent[n])
            self.Parent[n] = p
            return p

        def get_size(self, n):
            return self.size[self.get_Parent(n)]

        def merge(self, x, y):
            x = self.get_Parent(x)
            y = self.get_Parent(y)
            if x != y:
                if self.get_size(x) < self.get_size(y):
                    x, y = y, x
                self.size[x] += self.size[y]
                self.Parent[y] = x
                return True
            return False

        def is_united(self, x, y):
            return self.get_Parent(x) == self.get_Parent(y)

    U_row = UnionFind(N)
    for i in range(N):
        for j in range(i + 1, N):
            if U_row.is_united(i, j):
                continue
            for k in range(N):
                if A[i][k] + A[j][k] > K:
                    break
            else:
                U_row.merge(i, j)

    ans = 1
    for i in range(N):
        j = U_row.get_Parent(i)
        if i == j:
            tmp = 1
            s = U_row.get_size(i)
            for k in range(2, s + 1):
                tmp = tmp * k % MOD
            ans = ans * tmp % MOD
    return ans % MOD


ans = f(A) * f(B) % MOD
print(ans)
