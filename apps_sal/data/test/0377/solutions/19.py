n, m = list(map(int, input().split()))

if m == n:
    print(0)

elif m == 0 or m == 1:
    print(1)

else:
    m -= 1
    n -= 1
    print(min(m+1, n - m))

