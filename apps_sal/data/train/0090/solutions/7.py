
INF = float('inf')


def prod(arr):
    ret = 1
    for x in arr:
        ret *= x

    return ret


def tc():
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    uis = []
    for i in range(n):
        if not l[i]:
            uis.append(i)

    uvals = [a[i] for i in uis]
    uvals.sort()

    for i in uis:
        a[i] = uvals.pop()

    print(' '.join(map(str, a)))


T = int(input())
for _ in range(T):
    tc()
