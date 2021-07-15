x, k, d = map(int, input().split())
x = abs(x)

if x >= k*d:
    ans = x - k*d
else:
    c = x // d
    x %= d
    k -= c
    if k%2 == 0:
        ans = x
    else:
        ans = abs(x-d)

print(ans)
