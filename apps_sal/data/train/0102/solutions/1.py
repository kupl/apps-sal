t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    for i in range(1, 10):
        now = i
        while now <= n:
            now *= 10
            now += i
            ans += 1
    print(ans)
