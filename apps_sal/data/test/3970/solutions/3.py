from sys import stdin
__author__ = 'artyom'


def read_next_line():
    return list(map(int, stdin.readline().strip().split()))


(n, k) = read_next_line()
a = read_next_line()
res = set(a)
if k > 1:
    excl = set()
    for x in reversed(sorted(a)):
        if x % k > 0 or x in excl:
            continue
        p = x / k
        if p in res:
            res.remove(p)
            excl.add(p)
print(len(res))
