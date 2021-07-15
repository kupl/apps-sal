n, m = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(m):
    curr = 0
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        curr += a[j]
    if curr > 0:
        res += curr
print(res)
