
def f_f():
    n, *s = list(map(int, open(0).read().split()))
    s.sort()
    ps, next_ps, cs = [s.pop()], [], []
    for _ in range(n):
        for p in ps:
            while s:
                c = s.pop()
                if p > c:
                    next_ps.append(c)
                    break
                else:
                    cs.append(c)
        s, ps, next_ps, cs = s + cs[::-1], sorted(ps + next_ps, reverse=True), [], []

    print(("No" if s else "Yes"))


def __starting_point():
    f_f()


__starting_point()
