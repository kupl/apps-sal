(n, k, m, t) = map(int, input().split())
for j in range(t):
    (a, i) = map(int, input().split())
    if a:
        n += 1
        if i <= k:
            k += 1
    elif i >= k:
        n = i
    else:
        n -= i
        k -= i
    print(n, k)
