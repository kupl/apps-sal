def solve():
    n = int(input())
    h = [0] * n
    x = [0] * n
    for i in range(n):
        (x[i], h[i]) = map(int, input().split())
    ans = 2
    for i in range(1, n - 1):
        if x[i] - x[i - 1] > h[i]:
            ans += 1
        elif x[i + 1] - x[i] > h[i]:
            ans += 1
            x[i] += h[i]
    if n <= 2:
        ans = n
    print(ans)


solve()
