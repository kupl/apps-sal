N, M = map(int, input().split())
if N == 1:
    if M == 1:
        print(1)
    else:
        print(M-2)
elif N == 2:
    print(0)
else:
    if M == 1:
        print(N-2)
    else:
        print((N-2)*(M-2))
