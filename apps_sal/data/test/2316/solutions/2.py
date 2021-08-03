for i in range(int(input())):
    x, n, m = map(int, input().split())
    for i in range(n):
        a = x // 2 + 10
        x = min(x, a)
    for j in range(m):
        x -= 10
    print("YES" if x <= 0 else "NO")
