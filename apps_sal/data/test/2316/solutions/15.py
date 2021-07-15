

t = int(input())

for _ in range(t):
    x, n, m = list(map(int, input().split()))
    while x // 2 + 10 < x and n > 0:
        x = x // 2 + 10
        n -= 1

    while x > 0 and m > 0:
        x -= 10
        m -= 1

    print("NO" if x > 0 else "YES")

