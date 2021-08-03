input()

ll = list(input())

dd = {}


def is_up(s):
    return s.lower() != s


def is_lo(s):
    return s.lower() == s


ma = 0


for i in range(len(ll)):
    if is_up(ll[i]):
        dd = {}
    else:
        c = ll[i]
        if c not in dd:
            dd[c] = 1
        ma = max(len(dd), ma)

ma = max(len(dd), ma)

print(ma)
