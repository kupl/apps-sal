n, m = map(int, input().split())
a = [i for i in range(1, n + 1)]
used = [0] * (n + 1)
c = 0
t = 0


def gen(ind):
    nonlocal c, t
    if t:
        return
    if ind == n:
        s = 0
        for k in range(n):
            mi = a[k]
            for d in range(k, n):
                if mi > a[d]:
                    mi = a[d]
                s += mi
        if s == ma:
            c += 1
            if c == m:
                print(*a)
                t = 1
                return
        return
    for i in range(1, n + 1):
        if t:
            return
        if not used[i]:
            used[i] = 1
            a[ind] = i
            gen(ind + 1)
            a[ind] = 1
            used[i] = 0
    return


ma = 0
for i in range(n - 1, -1, -1):
    ma += (n - i) * a[i]
gen(0)
