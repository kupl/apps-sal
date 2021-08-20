t = int(input())
for _ in range(t):
    (a, b, n) = list(map(int, input().split()))
    ans = 0
    while a <= n and b <= n:
        ans += 1
        if a <= b:
            a += b
        else:
            b += a
    print(ans)
