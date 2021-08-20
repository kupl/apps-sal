t = int(input())
for _ in range(t):
    (x, y) = map(int, input().split())
    (a, b) = map(int, input().split())
    ans = min(b * min(x, y) + a * abs(x - y), a * (x + y))
    print(ans)
