(N, M) = map(int, input().split())
if N == 1:
    if M > 2:
        print(M - 2)
    elif M == 1:
        print(1)
    else:
        print(0)
elif N == 2 or M == 2:
    print(0)
elif M > 2:
    print((N - 2) * (M - 2))
elif M == 1:
    print(N - 2)
