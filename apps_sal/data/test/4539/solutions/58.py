N = int(input())


def keta_sum(N):
    if N < 10:
        return N
    else:
        return keta_sum(N // 10) + (N % 10)


if N % keta_sum(N) == 0:
    print('Yes')
else:
    print('No')
