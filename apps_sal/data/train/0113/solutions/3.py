t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))

    d = abs(b - a)
    ans = 0
    ans += d // 5
    d = d % 5
    ans += d // 2
    d %= 2
    ans += d // 1
    d %= 1

    print(ans)
