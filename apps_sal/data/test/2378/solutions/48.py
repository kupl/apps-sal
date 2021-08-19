N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    (A, B) = list(map(int, input().split()))
    E[A - 1].append(B - 1)
    E[B - 1].append(A - 1)
MOD = 10 ** 9 + 7
dp = [1] * N
root = 0
parent = [0] * N
order = []


def dfs():
    parent[root] = root
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        for ss in E[node]:
            if parent[node] != ss:
                stack.append(ss)
                parent[ss] = node


pow2 = [1] * (N + 1)
for i in range(1, len(pow2)):
    pow2[i] = pow2[i - 1] * 2 % MOD


def solve():
    ans = 0
    inv2 = pow(2, MOD - 2, MOD)
    p0 = pow(pow2[N - 1], MOD - 2, MOD)
    for i in reversed(order):
        if root != i:
            dp[parent[i]] += dp[i]
        p = 0
        if len(E[i]) >= 2:
            p1 = 1
            for s in E[i]:
                size = 0
                if parent[i] != s:
                    size = dp[s]
                elif i != root:
                    size = N - dp[i]
                else:
                    continue
                p1 += pow2[size] - 1
            p = 1 - p0 * p1
            p %= MOD
        ans += p
        ans %= MOD
    ans = ans * inv2 % MOD
    print(ans)


dfs()
solve()
