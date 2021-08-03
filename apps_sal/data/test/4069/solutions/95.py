x, k, d = list(map(int, input().split()))
if x < 0:
    x = -1 * x
if x >= k * d:
    print((x - k * d))
else:
    ans = (x - k * d) % (2 * d)
    if ans > d:
        print((2 * d - ans))
    else:
        print(ans)
