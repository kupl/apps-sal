from itertools import chain
C=0

def main():
    input()
    s = input()
    n = len(s)
    a = s[-1]
    for stop, b in enumerate(s):
        if b != a:
            break
    else:
        print('0' * n)
        return
    s = ''.join((s[stop:], s[:stop]))
    a, start = s[0], 0
    ma, l = 0, []
    for stop, b in enumerate(s):
        if b != a:
            le = stop - start
            #tail=9-(ord(b)-ord(a))%10
            if ma < le:
                ma = le
                l.clear()
                l.append(start)
            elif ma == le:
                l.append(start)
            a, start = b, stop
    le = n - start
    if ma < le:
        l.clear()
        l.append(start)
    elif ma == le:
        l.append(start)
    for i, start in enumerate(l):
        base = int(s[start])
        l[i] = ''.join(chr((int(c) - base) % 10 + 48) for c in chain(s[start:], s[:start]))
    print(min(l))


def __starting_point():
    main()
__starting_point()
