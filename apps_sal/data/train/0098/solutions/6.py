Q = int(input())
for q in range(Q):
    (c, m, x) = tuple(map(int, input().split()))
    ans = min(c, m)
    c -= ans
    m -= ans
    if c + m + x >= ans:
        print(ans)
        continue
    delta = (ans - (c + m + x)) * 2
    ans = c + m + x
    ans += min(delta // 3, delta // 2)
    print(ans)
