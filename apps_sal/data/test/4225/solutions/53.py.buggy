a, b, c, k = map(int, input().split())
ans = a
if k - a <= 0:
    print(k)
    return
if k - a - b <= 0:
    print(ans)
    return
if k - a - b - c < 0:
    ans = ans + (k - a - b) * (-1)
    print(ans)
else:
    ans = ans - c
    print(ans)
