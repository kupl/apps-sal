_ = int(input())
a = list(map(int, input().split()))
a.sort()
n = max(a)
a = a[:-1]
rc = float('inf')
rd = 0
r = 0
for i in a:
    if rc > abs(i - n / 2):
        r = i
    rc = min(rc, abs(i - n / 2))
print(n, r)
