import math
'\n26 6\n2 5\n\n\n'


def solution():
    (n, k) = list(map(int, input().strip().split()))
    a = []
    for i in range(k):
        mi = math.floor((2 * n / (k - i) + i + 1 - k) / 2)
        if mi < 0:
            break
        mi = 2 * a[-1] if len(a) > 0 and mi > 2 * a[-1] else mi
        a.append(mi)
        n -= mi
    if n != 0:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, a)))


while True:
    try:
        solution()
    except:
        break
