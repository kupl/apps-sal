M, K = list(map(int, input().split()))

if M < 2:
    if K != 0:
        print((-1))
    else:
        anss = []
        for A in range(2**M):
            anss += [A, A]
        print((' '.join(map(str, anss))))
else:
    if K > 2**M - 1:
        print((-1))
    else:
        anss = []
        for A in range(2**M):
            if A == K:
                continue
            anss.append(A)
        anss = anss + [K] + anss[::-1] + [K]
        print((' '.join(map(str, anss))))
