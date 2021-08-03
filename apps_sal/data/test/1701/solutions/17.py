def main():
    n, m = map(int, input().split())
    nms = {}
    for i in range(n):
        nm, ip = input().split()
        nms[ip] = nm
    for j in range(m):
        nm, ip = input().split()
        print('%s %s #%s' % (nm, ip, nms[ip[:-1]]))


def __starting_point():
    main()


__starting_point()
