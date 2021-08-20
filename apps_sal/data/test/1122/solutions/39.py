(N, M) = list(map(int, input().split()))
src = [i + 1 for i in range(M * 2 + 1)]
if M % 2 == 0:
    for m in range(M // 2):
        a = src[m]
        b = src[M - m]
        print('{} {}'.format(a, b))
    for m in range(M // 2):
        a = src[M + 1 + m]
        b = src[-(m + 1)]
        print('{} {}'.format(a, b))
else:
    for m in range(M // 2):
        a = src[m]
        b = src[M - 1 - m]
        print('{} {}'.format(a, b))
    for m in range(M - M // 2):
        a = src[M + m]
        b = src[-(m + 1)]
        print('{} {}'.format(a, b))
