t = int(input())
for _ in range(t):
    a, b, n = list(map(int, input().split()))
    ans = 0
    while max(a, b) <= n:
        a, b = a + b, max(a, b)
        ans += 1
    print(ans)
