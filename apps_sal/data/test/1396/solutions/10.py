import sys

f = sys.stdin
n, k, x, = list(map(int, f.readline().split()))

r = [int(it) for it in f.readline().split()]


def collaps(r, k):
    n = len(r)
    max_collaps = 0
    if n < k:
        return 0
    elif n == 1 and k == 1:
        return 1
    elif n == 1 and k > 1:
        return 0
    else:
        i = 1
        g = 1
        col = r[0]
        while (i < n):
            if r[i] == col:
                g += 1
            else:
                if g >= k:
                    max_collaps += g
                    col = r[i]
                    for kk in range(g):
                        del r[i - 1]
                        i -= 1
                    n = len(r)
                    if n > 1:
                        g = 1
                        i = 1
                        col = r[0]
                        continue
                    else:
                        break
                else:
                    g = 1
                    col = r[i]
            i += 1

        if g >= k:
            max_collaps += g
        return max_collaps


r1 = r[:]


nn = 0
res = 0
c1 = 0
for m in range(len(r)):
    if (nn == 0) and (r[m] == x):
        r1 = r[:]
        r1.insert(m, x)
        c1 = collaps(r1, 3) - 1
        if c1 > res:
            res = c1
        nn = 1
    elif (r[m] != x):
        nn = 0

print(res)
