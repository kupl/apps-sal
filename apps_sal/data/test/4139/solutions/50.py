
N = int(input())


def solve(s):
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(i) > 0 for i in '357') else 0

    for c in '753':
        ret += solve(s + c)

    return ret


print((solve("0")))
