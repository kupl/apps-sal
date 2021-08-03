from functools import reduce


def sol(l):
    if not "X" in l:
        return "0"
    l = l.replace("O", "0").replace("X", "1")
    res = ["%ix%i" % (12 // i, i) for i in (12, 6, 4, 3, 2, 1) if reduce(lambda x, y: x & y, [int(l[i * j:i * j + i], 2) for j in range(12 // i)], -1)]
    return ("%i %s" % (len(res), " ".join(res)))


n = int(input())
print("\n".join([sol(input()) for i in range(n)]))
