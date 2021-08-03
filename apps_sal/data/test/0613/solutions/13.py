
def baserepr(n, b):
    repr = []
    for j in range(70):
        repr.append(n % b)
        n //= b
    return repr


def tweaks(a, p):
    twk = [a]
    for i in range(len(a)):
        if (a[i] == 0 or i == 0):
            continue

        cur = list(a)
        cur[i] -= 1
        cur[i - 1] += p
        twk.append(cur)

    return twk


def evals(a, x):
    ans = 0
    xp = 1
    for coef in a:
        ans += coef * xp
        xp *= x
    return ans


def solve(p, q, r):
    if (p == 1 and q == 1):
        if (r == 1):
            print("inf")
        else:
            print(0)
        return

    if (p == 1):
        ans = 0
        rq = tweaks(baserepr(r, q), q)
        for p1 in rq:
            if (sum(p1) == q):
                ans += 1
        print(ans)
        return

    if (q == 1):
        if (r == 1):
            print(1)
        else:
            print(0)
        return

    qp = baserepr(q, p)
    rq = baserepr(r, q)

    tqp = tweaks(qp, p)
    trq = tweaks(rq, q)

    ans = 0

    for p1 in tqp:
        for p2 in trq:

            if (p1 != p2):
                continue

            # print(p1, ", ", p2)

            res1 = evals(p1, p)
            res2 = evals(p2, q)
            if (res1 == q and res2 == r):
                ans += 1

    print(ans)


p, q, r = map(int, input().split())
solve(p, q, r)
