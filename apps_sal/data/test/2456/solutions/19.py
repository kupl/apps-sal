t = int(input())
while t:
    (n, r) = list(map(int, input().split()))
    ans = 0
    if n <= r:
        ans += 1
    ans += min(n - 1, r) * (min(n - 1, r) + 1) // 2
    print(ans)
    t -= 1
