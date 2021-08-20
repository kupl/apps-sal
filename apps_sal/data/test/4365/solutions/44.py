N = int(input())
if N & 1:
    print((N // 2 + 1) * (N // 2))
else:
    print((N // 2) ** 2)
