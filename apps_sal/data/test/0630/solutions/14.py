from sys import setrecursionlimit
setrecursionlimit(10**6)
n, k = map(int, input().split())
a = list(map(int, input().split()))
save = [[] for i in range(0, len(a) + 1)]


def fun(pos):
    if save[pos] == []:
        left = max(pos - 1 - k, 0)
        right = min(pos + k, len(a))
        if a[pos - 1] != 0:
            new_set = fun(a[pos - 1])
            if new_set[-1][1] >= left:
                new_set[-1] = (new_set[-1][0], right)
            else:
                new_set.append(tuple([left, right]))
        else:
            new_set = [tuple([left, right])]
        save[pos] = new_set
        return new_set.copy()
    else:
        return save[pos].copy()


def enc(a):
    z = 0
    for i in a:
        z = z + i[1] - i[0]
    return z


for i in range(1, len(a) + 1):
    print(enc(fun(i)), end=' ')
