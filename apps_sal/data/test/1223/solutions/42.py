import sys
input = sys.stdin.readline
n = int(input())
a = [int(j) for j in input().split()]
ans = 0
ind = [0] * (n + 1)
for i in range(n):
    ind[a[i]] = i + 1
l = [0] + list(range(n + 1))
r = list(range(1, n + 2)) + [n + 1]
for i in range(1, n + 1):
    l1 = l[ind[i]]
    l0 = l[l1]
    r0 = r[ind[i]]
    r1 = r[r0]
    ans += ((l1 - l0) * (r0 - ind[i]) + (r1 - r0) * (ind[i] - l1)) * i
    l[r0] = l1
    r[l1] = r0
print(ans)
