from sys import stdin
from datetime import datetime, timedelta


def main():
    s = stdin.readline().strip()
    t = stdin.readline().strip()
    s = datetime.strptime(s, '%H:%M')
    t = datetime.strptime(t, '%H:%M')
    t = timedelta(hours=t.hour, minutes=t.minute)
    p = s - t
    print('{:02}:{:02}'.format(p.hour, p.minute))


def __starting_point():
    main()


__starting_point()
