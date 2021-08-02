import sys
3


n, k, d = list(map(int, sys.stdin.readline().split()))

x = 1
while x ** d < n:
    x += 1

if x > k:
    sys.stdout.write("-1\n")
    return

ans = [[1 for i in range(d)] for j in range(n)]
for i in range(1, n):
    for j in range(d):
        ans[i][j] = ans[i - 1][j]
    ans[i][d - 1] += 1
    memo = 0
    for j in range(d - 1, -1, -1):
        ans[i][j] += memo
        memo = 0
        if ans[i][j] > x:
            memo = ans[i][j] - x
            ans[i][j] = 1

for i in range(d):
    sys.stdout.write(' '.join([str(ans[j][i]) for j in range(n)]) + '\n')
