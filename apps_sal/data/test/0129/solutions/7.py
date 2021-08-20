(n, m, k, l) = list(map(int, input().split()))
if l > n - k:
    print(-1)
else:
    am = (l + k) // m + bool((l + k) % m)
    if am * m > n:
        print(-1)
    else:
        print(am)
