for _ in range(int(input())):
    (n, m, k) = list(map(int, input().split()))
    H = list(map(int, input().split()))
    ans = 'YES'
    for i in range(n - 1):
        h1 = H[i]
        h2 = H[i + 1]
        if h1 >= h2:
            if h2 >= k:
                m += h1 - h2 + k
            else:
                m += h1
        elif h2 > h1 + m + k:
            ans = 'NO'
            break
        elif h2 <= k:
            m += h1
        elif h2 - h1 <= k:
            m += k - (h2 - h1)
        else:
            m -= h2 - h1 - k
    print(ans)
