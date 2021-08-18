n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

m = 0


def f(a, l, r):
    seq = a[l:r]
    ret = 0
    for i in seq:
        ret |= i
    return ret


print(f(a, 0, len(a)) + f(b, 0, len(b)))
