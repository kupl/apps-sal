import sys
3


n, k, d = list(map(int, sys.stdin.readline().split()))

x = 1
while x ** d < n:
    x += 1

if x > k:
    sys.stdout.write("-1\n")
    return

ans = [[1 for i in range(n)] for j in range(d)]
for i in range(1, n):
    for j in range(d):
        ans[j][i] = ans[j][i - 1]
    ans[d - 1][i] += 1
    memo = 0
    for j in range(d - 1, -1, -1):
        ans[j][i] += memo
        memo = 0
        if ans[j][i] > x:
            memo = ans[j][i] - x
            ans[j][i] = 1

for i in range(d):
    sys.stdout.write(' '.join(map(str, ans[i])) + '\n')
