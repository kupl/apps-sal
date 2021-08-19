(n, m) = map(int, input().split())
a = [int(x) for x in input().split()]
ans = 0
a = [1] + a
for i in range(1, len(a)):
    if a[i] >= a[i - 1]:
        ans += a[i] - a[i - 1]
    else:
        ans += n - a[i - 1] + a[i]
print(ans)
