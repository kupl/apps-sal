

arr = input()
N, K, M, T = [int(x) for x in arr.split(' ')]

uni = [0] * N

uni[K - 1] = 1

for i in range(T):
    arr = input()
    move, pos = [int(x) for x in arr.split(' ')]

    if move == 0:
        u1 = uni[:pos]
        u2 = uni[pos:]
        if 1 in u1:
            uni = u1
        else:
            uni = u2
            K -= len(u1)

        print(len(uni), K)

    else:
        p = pos - 1
        u1 = uni[:p]
        u2 = uni[p:]
        uni = u1 + [0] + u2

        if 1 in u2:
            K += 1

        print(len(uni), K)
