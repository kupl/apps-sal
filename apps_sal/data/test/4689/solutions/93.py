k, n = map(int, input().split())
a = list(map(int, input().split()))

bef = a[0]
max_diff = 0
for i in range(1,n):
    diff = abs(bef - a[i])
    max_diff = max(diff, max_diff)
    bef = a[i]

print(k - max(max_diff, k - abs(a[n-1] - a[0])))
