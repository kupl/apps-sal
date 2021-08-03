M, K = list(map(int, input().split()))

if K == 0:
    print((*(list(range(2 ** M)) + list(range(2 ** M - 1, -1, -1)))))
else:
    if M <= 1:
        print((-1))
    elif K.bit_length() > M:
        print((-1))
    else:
        index = 0
        used = [False] * (2 ** M)
        ans = []
        for _ in range(2 ** (M - 2)):
            while index < 2 ** M and used[index]:
                index += 1
            A = index
            C = index ^ K
            used[index] = True
            used[index ^ K] = True
            while index < 2 ** M and used[index]:
                index += 1
            B = index
            D = index ^ K
            used[index] = True
            used[index ^ K] = True
            ans += [A, C, B, D, C, A, D, B]
        print((*ans))
