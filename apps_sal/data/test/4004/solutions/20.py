import collections


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    c = collections.Counter(A)
    ck = list(c.keys())
    ck.sort()
    ck_len = len(ck)
    if ck_len >= 4:
        return -1
    elif ck_len == 3:
        if ck[2] - ck[1] == ck[1] - ck[0]:
            return ck[2] - ck[1]
        else:
            return -1
    elif ck_len == 2:
        if (ck[1] - ck[0]) % 2 == 0:
            return (ck[1] - ck[0]) // 2
        else:
            return ck[1] - ck[0]
    else:
        return 0


print(solve())
