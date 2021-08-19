q = int(input())
for i in range(q):
    (c, m, x) = map(int, input().split())
    ans = min(c, m, x)
    c -= ans
    m -= ans
    x -= ans
    ans += min(c, m, (c + m) // 3)
    print(ans)
