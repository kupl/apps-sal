n, k, m, t = list(map(int, input().split()))

for req in range(t):
    q, i = list(map(int, input().split()))
    if q == 1:
        n += 1
        if i <= k:
            k += 1
    else:
        if i >= k:
            n = i
        else:
            n -= i
            k -= i
    print(n, k)

