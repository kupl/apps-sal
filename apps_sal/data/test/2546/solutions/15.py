from sys import stdin, stdout


def fun1(n, m, l, s):
    cl = 0
    cr = 0
    cm = 0
    for i in range(n):
        if l[i][1] < m:
            s -= l[i][0]
            cl += 1
        elif l[i][0] > m:
            s -= l[i][0]
            cr += 1
        else:
            cm += 1
            if cm + cr <= 1 + n // 2:
                s -= m
            else:
                s -= l[i][0]
        if s < 0 or cr > n // 2 or cl > n // 2:
            return 0
    return 1


def search(n, low, high, l, su):
    l1 = l[::-1]
    while low < high:
        mid = (low + high) // 2
        if fun1(n, mid, l1, su):
            low = mid + 1
        else:
            high = mid
    if fun1(n, low, l1, su):
        return low
    return low - 1


def main():
    for _ in range(int(stdin.readline())):
        (n, su) = [int(x) for x in stdin.readline().split()]
        l = [[-1, -1] for i in range(n)]
        l2 = [-1 for i in range(n)]
        for i in range(n):
            inp = [int(j) for j in stdin.readline().split()]
            l[i] = inp
            l2[i] = inp[0]
        l.sort()
        low = int(l[n // 2][0])
        print(search(n, low, 10 ** 9 + 1, l, su))


def __starting_point():
    main()


__starting_point()
