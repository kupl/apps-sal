import sys

a = []
b = []
c = []
d = []


def main():
    #sys.stdin = open('D:\\Sublime\\in.txt', 'r')
    #sys.stdout = open('D:\\Sublime\\out.txt', 'w')

    n = int(sys.stdin.readline().strip('\n'))

    for i in range(n):
        opt, num = [int(line) for line in sys.stdin.readline().strip('\n').split()[:2]]
        if opt == 0:
            a.append(num)
        if opt == 10:
            b.append(num)
        if opt == 1:
            c.append(num)
        if opt == 11:
            d.append(num)

    res = sum(d)

    b.sort(reverse=True)
    c.sort(reverse=True)

    if len(b) > len(c):
        res += sum(c) + sum(b[:len(c)])
        a.extend(b[len(c):])
    else:
        res += sum(b) + sum(c[:len(b)])
        a.extend(c[len(b):])

    a.sort(reverse=True)
    res += sum(a[:len(d)])
    print(res)


def __starting_point():
    main()


__starting_point()
