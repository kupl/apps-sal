s = input()
t = input()

ss = sorted(s)
tt = sorted(t, reverse=True)


def checker(s, t):
    for sz in ss:
        for tz in tt:
            if sz > tz:
                return 'No'
            elif sz == tz:
                continue
            else:
                return 'Yes'
    if len(ss) < len(tt):
        return 'Yes'
    return 'No'


print((checker(ss, tt)))

