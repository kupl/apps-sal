

for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))

    ans = 0

    while(max(a, b) <= n):
        a, b = max(a, b), min(a, b)
        ans += 1
        b += a

    print(ans)
