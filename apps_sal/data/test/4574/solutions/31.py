import sys

n, *a = list(map(int, sys.stdin.read().split()))

a.sort(reverse=True)
c = 0
f = 0
ans = []
for i in range(n - 1):
    if a[i] == a[i + 1]:
        c += 1
        f += 1
        ans.append(a[i])
    else:
        f = 0
    if (c > 1 and f == 1) or (c > 2 and f == 3):
        print((ans[0] * ans[-1]))
        return
print((0))
