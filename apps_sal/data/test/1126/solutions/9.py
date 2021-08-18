import sys

readline = sys.stdin.readline


def solve(n, x, m):
    a = [x]
    a_set = {x}
    ai = x
    for _ in range(m):
        ai = ai ** 2 % m
        if ai in a_set:
            start = a.index(ai)
            loop = a[start:]
            lall = len(a)
            lloop = len(loop)
            break
        else:
            a.append(ai)
            a_set.add(ai)

    if n - 1 <= lall:
        ans = sum(a[:n])
    else:
        q, r = divmod(n - lall, lloop)
        ans = sum(a) + sum(loop) * q + sum(loop[:r])

    return ans


n, x, m = map(int, readline().split())
print(solve(n, x, m))
