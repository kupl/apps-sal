x, k, d = list(map(int, input().split()))
x = abs(x)

if x < k * d:
    step = x // d
    k -= step
    x -= step * d
    ans = x
    if k % 2 == 1:
        ans = abs(x - d)
else:
    x -= k * d
    ans = x

print(ans)
