from itertools import product


def next(p, o, a):
    for i in range(4):
        if (p | i == o and p & i == a):
            return i


def check(t):
    for j in range(n - 1):
        if not (t[j] | t[j + 1] == a[j] and t[j] & t[j + 1] == b[j]):
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
for j in range(4):
    t = [j]
    for i in range(1, n):
        nxt = next(t[-1], a[i - 1], b[i - 1])
        if nxt is None:
            break
        t.append(nxt)
    else:
        print('YES')
        print(' '.join(str(i) for i in t))
        break
else:
    print('NO')
