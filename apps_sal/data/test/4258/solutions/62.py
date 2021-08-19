(a, b, t) = list(map(int, input().split()))
ans = 0
now = a
while now <= t:
    ans += b
    now += a
print(ans)
