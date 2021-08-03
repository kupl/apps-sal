import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n = ni()
a = na()
M = max(a)
m = min(a)
ans = []

if m >= 0:
    for i in range(1, n):
        a[i] += a[i - 1]
        ans.append((i, i + 1))
else:
    if M <= 0:
        for i in range(n - 1)[::-1]:
            a[i] += a[i + 1]
            ans.append((i + 2, i + 1))
    else:
        if M > -m:
            Mi = a.index(M)
            for i in range(n):
                if a[i] < 0:
                    a[i] += M
                    ans.append((Mi + 1, i + 1))
            for i in range(1, n):
                a[i] += a[i - 1]
                ans.append((i, i + 1))
        else:
            mi = a.index(m)
            for i in range(n):
                if a[i] > 0:
                    a[i] += m
                    ans.append((mi + 1, i + 1))
            for i in range(n - 1)[::-1]:
                a[i] += a[i + 1]
                ans.append((i + 2, i + 1))

print(len(ans))
print('\n'.join([str(i) + ' ' + str(j) for i, j in ans]))
