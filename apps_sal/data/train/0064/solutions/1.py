for __ in range(int(input())):
    n, l = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    i, j = 0, n - 1
    x, y = 0, l
    v1, v2 = 1, 1
    ans = 0
    while i <= j and x < y:
        if (ar[i] - x) / v1 < (y - ar[j]) / v2:
            ans += (ar[i] - x) / v1
            y -= v2 * (ar[i] - x) / v1
            x = ar[i]
            v1 += 1
            i += 1
        else:
            ans += (y - ar[j]) / v2
            x += v1 * (y - ar[j]) / v2
            y = ar[j]
            v2 += 1
            j -= 1
    ans += (y - x) / (v1 + v2)
    print(ans)
