import datetime
import sys


def __starting_point():
    for l in sys.stdin:
        a = tuple((int(i) for i in l.strip().split(':')))
        s = datetime.date(*a)
        break
    for l in sys.stdin:
        a = tuple((int(i) for i in l.strip().split(':')))
        e = datetime.date(*a)
        break
    print(abs((e - s).days))


__starting_point()
