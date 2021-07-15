import sys
sys.setrecursionlimit(500*500)
n = int(input())
a = [[] for _ in range(n)]; b = [-1]*n; b[0] = 0
for i in range(n-1):
    u, v, w = map(int, input().split())
    a[u-1].append([v-1, w]); a[v-1].append([u-1, w])
def dfs(A, k):
    for i in A[k]:
        if b[i[0]] == -1:
            b[i[0]] = b[k]+i[1]
            dfs(A, i[0])
dfs(a, 0)
for i in b:
    print(0) if i%2 == 0 else print(1)
