t = int(input())
for i in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    b //= 2
    ans = 0
    for i in range(b + 1):
        ans = max(ans, min(p, i) * h + min(f, b - i) * c)
    print(ans)
