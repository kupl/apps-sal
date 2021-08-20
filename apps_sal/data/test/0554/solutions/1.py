(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(m):
    (left, right) = list(map(int, input().split()))
    sm = 0
    for i in range(left - 1, right):
        sm += a[i]
    if sm > 0:
        ans += sm
print(ans)
