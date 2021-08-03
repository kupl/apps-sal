ks = [int(v) for v in input().split()]
ks.sort()


def solve(ks):
    k1, k2, k3 = ks

    if k1 == 1:
        return True
    elif k1 == 2:
        if k2 == 2:
            return True
        elif k2 == 4 and k3 == 4:
            return True
        else:
            return False
    elif k1 == 3:
        if k2 == 3 and k3 == 3:
            return True
        else:
            return False
    else:
        return False


print(["NO", "YES"][solve(ks)])
