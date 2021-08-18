
n = int(input())
a = list(map(int, input().split()))


def func(x):
    b = list(a)
    r = []
    for i in range(n):

        if x % 3 == 0 and x // 3 in b:
            x //= 3
            b.remove(x)
            r += [x]
        if x * 2 in b:
            x *= 2
            b.remove(x)
            r += [x]
    return r


for i in a:
    if sorted([i] + func(i)) == sorted(a):
        print(' '.join(map(str, [i] + func(i))))
