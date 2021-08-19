(N, M) = list(map(int, input().split()))
if N < 2 or M < 2:
    if N == M:
        print(1)
    else:
        print(max(N, M) - 2)
elif N == 2 or M == 2:
    print(0)
else:
    print((N - 2) * (M - 2))
