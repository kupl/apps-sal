
def m(s1, s2):
    si = s1.intersection(s2)
    if si:
        return min(si)
    smin, smax = sorted(map(min, (s1, s2)))
    return smin * 10 + smax


def __starting_point():
    input()
    print(m(*(set(map(int, input().split())) for i in range(2))))


__starting_point()
