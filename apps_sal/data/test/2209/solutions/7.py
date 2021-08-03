import functools


def cmp(a, b):
    if (a.count('s') / len(a)) < (b.count('s') / len(b)):
        return 1

    else:
        return -1


n = int(input())
a = [input() for i in range(n)]

a = sorted(a, key=functools.cmp_to_key(cmp))


a = ''.join(a)

c = 0
t = 0

for i in a:
    if i == 's':
        c += 1
    else:
        t += c

print(t)
