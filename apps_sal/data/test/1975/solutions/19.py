n, m = list(map(int, input().split()))
print(n + m - 1)
if n + m == 1: print(1, 1)
elif m > 1:
    for i in range(1, n + 1): print(i, 1)
    for i in range(2, m + 1): print(1, i)
else:
    for i in range(2, n + 1): print(i, 1)
    for i in range(1, m + 1): print(1, i)
