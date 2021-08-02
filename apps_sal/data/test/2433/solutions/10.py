T = int(input())
for i in range(T):
    b, p, f = list(map(int, input().split()))
    h, c = list(map(int, input().split()))
    ans = 0
    if h > c:
        bur = min(b // 2, p)
        ans += h * bur
        b -= bur * 2

        ans += min(b // 2, f) * c
    else:
        fish = min(b // 2, f)
        ans += c * fish
        b -= fish * 2

        ans += min(b // 2, p) * h
    print(ans)
