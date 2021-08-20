(M, K) = map(int, input().split())


def binary_digits(n):
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 2
    return cnt


if binary_digits(K) > M:
    print(-1)
elif M == 1:
    if K == 1:
        print(-1)
    elif K == 0:
        print(0, 0, 1, 1)
else:
    b = 2 ** (M + 1)
    if K == 0:
        for i in range(b):
            if i != b - 1:
                print(i // 2, end=' ')
            else:
                print(i // 2)
    else:
        A = [0 for i in range(b)]
        (A[1], A[b // 2 + 1]) = (K, K)
        p = 1
        for i in range(1, b // 2):
            if i != K:
                (A[b // 2 - p + 1], A[b // 2 + p + 1]) = (i, i)
                p += 1
        for i in range(b):
            if i != b - 1:
                print(A[i], end=' ')
            else:
                print(A[i])
