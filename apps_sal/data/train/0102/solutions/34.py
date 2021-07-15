t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(1, len(str(n)) + 1):
        for j in range(1, 10):
            if (int(str(j) * i) <= n):
                ans += 1
    print(ans)

