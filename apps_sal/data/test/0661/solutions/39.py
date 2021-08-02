M, K = map(int, input().split())

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
elif K < (1 << M):
    for i in range(1 << M):
        if i != K:
            print(i, end=" ")
    print(K, end=" ")
    for i in range((1 << M) - 1, -1, -1):
        if i != K:
            print(i, end=" ")
    print(K)
else:
    print(-1)
