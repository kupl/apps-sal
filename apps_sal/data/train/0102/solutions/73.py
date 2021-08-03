q = int(input())

for _ in range(q):
    n = int(input())
    z = 10
    k = 1
    ans = 0
    x = 1
    while z <= n:
        x = x * 10 + 1
        z *= 10
        k += 1
        ans += 9
    k = 1
    while n >= x * k:
        k += 1
    print(ans + k - 1)
