for _ in range(int(input())):
    (x1, y1, z1) = list(map(int, input().split()))
    (x2, y2, z2) = list(map(int, input().split()))
    k = min(z1, y2)
    ans = k * 2
    z1 -= k
    y2 -= k
    k = min(z2, x1)
    z2 -= k
    x1 -= k
    z2 -= z1
    if z2 > 0:
        ans -= z2 * 2
    print(ans)
