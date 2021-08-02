import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n, m, h = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = [list(map(int, input().split())) for i in range(n)]
ans = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if x[i][j] == 1:
            ans[i][j] = min(b[i], a[j])
for i in range(n):
    print(*ans[i])
