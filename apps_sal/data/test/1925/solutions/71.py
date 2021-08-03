A, B, N = list(map(int, input().split()))

if N < B:
    print((int(((A * N) / B) - ((A * N) / B) % 1 - A * (N / B - (N / B) % 1))))
else:
    print((int(((A * (B - 1)) / B) - ((A * (B - 1)) / B) % 1 - A * ((B - 1) / B - ((B - 1) / B) % 1))))
