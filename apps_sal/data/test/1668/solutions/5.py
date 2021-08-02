import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    n = int(I())
    c = 0
    l = [I() for _ in range(n)]
    r = []
    for s in l:
        if s in r:
            c += 1
            for i in range(10):
                sn = s[:-1] + chr(ord('0') + i)
                if sn not in l and sn not in r:
                    s = sn
                    break
        r.append(s)
    print(c)
    for s in r:
        print(s)
