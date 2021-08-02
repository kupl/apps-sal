k, p = list(map(int, input().split()))
ans = 0
for n in range(1, k + 1):
    x = n
    y = 0
    z = n
    while 0 < x:
        y *= 10
        y += x % 10
        x //= 10
        z *= 10
    z += y
    ans += z
    ans %= p
print(ans)
