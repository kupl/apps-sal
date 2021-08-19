t = int(input())
for i in range(t):
    (n, m, k) = map(int, input().split())
    h = list(map(int, input().split()))
    for i in range(n - 1):
        if h[i] >= h[i + 1] - k:
            m += min(h[i] - (h[i + 1] - k), h[i])
        elif m >= h[i + 1] - k - h[i]:
            m -= h[i + 1] - k - h[i]
        else:
            print('NO')
            break
    else:
        print('YES')
