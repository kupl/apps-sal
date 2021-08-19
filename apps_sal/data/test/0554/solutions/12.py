(n, m) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
ans = 0
for z in range(m):
    (l, r) = [int(i) for i in input().split()]
    sum = 0
    for i in range(l - 1, r):
        sum += a[i]
    if sum > 0:
        ans += sum
print(ans)
