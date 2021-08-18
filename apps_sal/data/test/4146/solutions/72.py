import collections as co


def __starting_point():

    n = int(input())
    A = list(map(int, input().split()))

    S = A[1::2]
    T = A[0::2]

    total_cnt = 0

    U = set(A)
    if len(U) == 1:
        total_cnt = len(A[1::2])
        print(total_cnt)
        return

    c1 = []
    c2 = []
    s = co.Counter(S)
    c1 = s.most_common()
    c1.append((0, 0))
    t = co.Counter(T)
    c2 = t.most_common()
    c2.append((0, 0))

    if c1[0][0] != c2[0][0]:
        total_cnt = len(S) - c1[0][1]
        total_cnt += len(T) - c2[0][1]
    else:
        if c1[0][1] > c2[0][1]:
            total_cnt = len(S) - c1[0][1]
            total_cnt += len(T) - c2[1][1]
        elif c1[0][1] < c2[0][1]:
            total_cnt = len(S) - c1[1][1]
            total_cnt += len(T) - c2[0][1]
        else:
            if c1[1][1] > c2[0][1]:
                total_cnt = len(S) - c1[1][1]
                total_cnt += len(T) - c2[0][1]
            elif c1[1][1] < c2[1][1]:
                total_cnt = len(T) - c2[1][1]
                total_cnt += len(S) - c1[0][1]
            else:
                total_cnt = len(S) - c1[1][1]
                total_cnt += len(T) - c2[0][1]

    print(total_cnt)


__starting_point()
