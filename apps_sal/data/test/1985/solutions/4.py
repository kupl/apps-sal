from itertools import accumulate
k, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
suma = list(accumulate(a))


def possible(s):
    target = set(b)
    for i in a:
        s += i
        if s in target:
            target.remove(s)
    return not target


pos = set()
for i in range(k):
    ini = b[0] - suma[i]
    if possible(ini):
        pos.add(ini)
print(len(pos))
