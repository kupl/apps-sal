(L, R) = list(map(int, input().split()))
if R - L > 2019:
    print(0)
else:
    x = 2019
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            x = min(x, i * j % 2019)
    print(x)
