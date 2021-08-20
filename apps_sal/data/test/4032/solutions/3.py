(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
while len(a) > 0 and a[0] <= k:
    ans += 1
    a = a[1:]
while len(a) > 0 and a[-1] <= k:
    ans += 1
    a = a[:-1]
print(ans)
