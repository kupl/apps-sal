t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    for i in range(n):
        if (x // 2 + 10) >= x:
            break
        x //= 2
        x += 10
    for i in range(m):
        x -= 10
        if x <= 0:
            break
    if x <= 0:
        print("YES")
    else:
        print("NO")
