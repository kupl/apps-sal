import sys


def dfs(A: list):
    if len(A) == n:
        for i in range(len(A) - 1):
            if A[i + 1] not in node[A[i]]:
                break
            if i == n - 2:
                ans[0] += 1
        return
    for v in range(2, n + 1):
        if v not in A:
            A.append(v)
            dfs(A)
            A.pop()


n, m = list(map(int, input().split()))
node = [set() for _ in range(n + 1)]
for x in sys.stdin.readlines():
    a, b = list(map(int, x.split()))
    node[a].add(b)
    node[b].add(a)
ans = [0]
dfs([1])
print((ans[0]))
