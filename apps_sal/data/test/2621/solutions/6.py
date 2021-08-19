for t in range(int(input())):
    (n, m, k) = list(map(int, input().split()))
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] >= h[i + 1] - k:
            m += h[i] - max(0, h[i + 1] - k)
        elif h[i] + m < h[i + 1] - k:
            print('NO')
            break
        else:
            m -= h[i + 1] - k - h[i]
    else:
        print('YES')
