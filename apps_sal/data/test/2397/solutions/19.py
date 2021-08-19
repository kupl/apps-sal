import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = 0
p = []
for i in range(n - 1, 0, -1):
    s += a[i]
    p.append(s)
p.sort()
p.reverse()
res = s + a[0]
for i in range(k - 1):
    res += p[i]
print(res)
