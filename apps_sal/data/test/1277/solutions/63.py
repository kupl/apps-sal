import sys


def dfs(c, lst):
    n = len(lst)
    ans = [0] * n
    stack = [c - 1]
    check = [0] * n
    while stack != []:
        d = stack.pop()
        if check[d] == 0:
            check[d] = 1
            for i in lst[d]:
                if check[i] == 0:
                    stack.append(i)
                    ans[i] = ans[d] + 1
    return ans


input = sys.stdin.readline
(N, u, v) = list(map(int, input().split()))
ki = [[] for f in range(N)]
for i in range(N - 1):
    (a, b) = list(map(int, input().split()))
    ki[a - 1].append(b - 1)
    ki[b - 1].append(a - 1)
U = dfs(u, ki)
V = dfs(v, ki)
ans = 0
for i in range(N):
    if V[i] > U[i]:
        ans = max(ans, V[i] - 1)
print(ans)
