(M, K) = map(int, input().split())
if M == 0:
    if K == 0:
        print(0, 0)
    else:
        print(-1)
elif M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
elif K == 0:
    A = [i // 2 for i in range(2 ** (M + 1))]
    print(*A)
elif 0 < K < 2 ** M:
    A = []
    for i in range(K):
        A.append(i)
    for i in range(2 ** M - K - 1):
        A.append(2 ** M - i - 1)
    A.append(0)
    for i in range(2 ** M - K):
        A.append(K + i)
    for i in range(K - 1):
        A.append(K - i - 1)
    A.append(K)
    print(*A)
else:
    print(-1)
