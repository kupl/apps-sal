x, k, d = list(map(int, input().split()))
x = abs(x)
ans = 0
if x // d > k:
    ans = x - d * k
else:
    e = x // d
    k -= e
    x -= e * d
    if (k % 2 == 1):
        x = abs(x - d)
    ans = x
print(ans)

