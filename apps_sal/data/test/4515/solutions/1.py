t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())

    m = max(a, b, c)

    su = m - a + m - b + m - c

    if n < su:
        print("NO")
        continue

    n -= su
    if n % 3 == 0:
        print("YES")
    else:
        print("NO")
