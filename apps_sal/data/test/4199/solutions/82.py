(n, k) = map(int, input().split())
a = list(map(int, input().split()))
o = 0
i = 0
for i in range(n):
    if a[i] >= k:
        o += 1
print(o)
