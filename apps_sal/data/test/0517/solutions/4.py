n, d, h = list(map(int, input().split()))
if n == 2 and d == h and d == 1:
    print(1, 2)
elif h * 2 < d or d == 1 or (h == 1 and d != 2):
    print(-1)
elif h == 1 and d == 2:
    k = 2
    while k != n + 1:
        print(1, k)
        k += 1
else:
    k = 0
    i = 1
    j = 2
    while k != h:
        print(i, j)
        i += 1
        j += 1
        k += 1
    i = 1
    k = 0
    while k < d - h:
        print(i, j)
        i = j
        j += 1
        k += 1
    k += h
    while k < n - 1:
        print(2, j)
        j += 1
        k += 1
