m, n = list(map(int, input().split()))
if (m + n) != 3:
    print(abs(m - n))
else:
    print(m + n)
