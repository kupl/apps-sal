n, m = list(map(int, input().split()))

oddflag = True
for i in range(1, m + 1):
    mid = (1 + n) // 2
    if oddflag:
        oddflag = False
        print((i // 2 + 1, n - i // 2))
    else:
        oddflag = True
        print((mid + i // 2, mid - i // 2))
