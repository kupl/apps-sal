N, *AB = list(map(int, open(0).read().split()))
A = sorted(a for a in AB[::2])
B = sorted(b for b in AB[1::2])
if N % 2:
    print((B[N // 2] - A[N // 2] + 1))
else:
    print((B[N // 2 - 1] + B[N // 2] - A[N // 2 - 1] - A[N // 2] + 1))
