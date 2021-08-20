(n, k, m, t) = list(map(int, input().split()))
for i in range(t):
    (a, b) = list(map(int, input().split()))
    if a:
        if b <= k and n + 1 <= m:
            k += 1
            n += 1
        elif b > k and n + 1 <= m:
            n += 1
    elif b < k:
        k -= b
        n -= b
    elif b >= k:
        n -= n - b
    print(n, k)
