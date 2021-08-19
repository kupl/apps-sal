n = int(input())
for i in range(n):
    ans = 0
    (x, y) = list(map(int, input().split()))
    if y > x:
        (x, y) = (y, x)
    while y > 0:
        ans += x // y
        x = x % y
        (x, y) = (y, x)
    print(ans)
