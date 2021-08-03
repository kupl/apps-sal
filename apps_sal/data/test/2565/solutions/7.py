for nt in range(int(input())):
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())
    a = min(x1, z2)
    z2, x1 = z2 - a, x1 - a
    if z2 == 0:
        ans = min(z1, y2) * 2
    else:
        z1, z2 = z1 - min(z1, z2), z2 - min(z1, z2)
        if z2 == 0:
            ans = min(z1, y2) * 2
        else:
            ans = -(z2 * 2)
    print(ans)
