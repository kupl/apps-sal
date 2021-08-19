t = int(input())
for gg in range(t):
    (a, b) = list(map(int, input().split()))
    d = abs(a - b)
    if d == 0:
        print(0)
    else:
        ans = 0
        ans += d // 5
        d %= 5
        ans += d // 2
        d %= 2
        ans += d
        print(ans)
