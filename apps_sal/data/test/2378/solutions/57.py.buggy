import sys
sys.setrecursionlimit(1000000)
readline = sys.stdin.readline

N = int(readline())

adj = [[] for i in range(N)]
for i in range(N - 1):
    A, B = list(map(int, readline().split()))
    A -= 1
    B -= 1
    adj[A].append(B)
    adj[B].append(A)

mod = 10 ** 9 + 7
pow2 = [1] * (N + 1)
for i, j in zip(list(range(N)), list(range(1, N + 1))):
    pow2[j] = pow2[i] * 2 % mod

ans = 0


def dfs(node, parent):
    nonlocal ans
    cnt = 1

    for child in adj[node]:
        if child != parent:
            cnt += dfs(child, node)

    ans += (pow2[cnt] - 1) * (pow2[N - cnt] - 1)
    ans %= mod

    return cnt


dfs(0, None)

ans = (ans - N * pow2[N - 1] + pow2[N] - 1) % mod
ans = ans * pow(pow2[N], mod - 2, mod) % mod

print(ans)
