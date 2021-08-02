t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    while n > 0 and x > 10:
        x = x // 2 + 10
        n -= 1
    while m > 0:
        x -= 10
        m -= 1
    if x <= 0:
        print("YES")
    else:
        print("NO")
