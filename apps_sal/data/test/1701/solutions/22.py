from pprint import pprint as pp
def GI(): return int(input())
def GIS(): return list(map(int, input().split()))


def main():
    n, m = GIS()

    d = {}
    for i in range(n):
        name, ip = input().split()
        d[ip] = name

    for i in range(m):
        s = input()
        ip = s.split()[1][:-1]
        print('%s #%s' % (s, d[ip]))


main()
