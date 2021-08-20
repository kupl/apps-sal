t = int(input())
for i in range(t):
    (a, b, c) = list(map(int, input().split()))
    ans = 0
    for t1 in range(a + 1):
        for t2 in range(b + 1):
            if a - t1 >= 0 and b - 2 * t1 - t2 >= 0 and (c - 2 * t2 >= 0):
                ans = max(ans, 3 * (t1 + t2))
    print(ans)
