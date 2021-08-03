N, D = map(int, input().split())
R = N % (2 * D + 1)
if R != 0:
    L = (N - R) / (2 * D + 1) + 1
else:
    L = N / (2 * D + 1)
print(int(L))
