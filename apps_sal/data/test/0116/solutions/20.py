import sys


def readnlines(f_in):
    n = int(f_in.readline().strip())
    m = []
    for i in range(n):
        line = f_in.readline().strip()
        if line.isdigit():
            m.append(int(line))
        else:
            m.append(line)
    return m


def print_args():
    print('Recieved {} arguments = {}.'.format(len(sys.argv), sys.argv))


def intersect(l1, r1, l2, r2):
    left = max(l1, l2)
    right = min(r1, r2)
    return (left, right, max(0, right - left + 1))


def solve():
    line = sys.stdin.readline().strip()
    (l1, r1, l2, r2, k) = [int(i) for i in line.split()]
    (left, right, inters) = intersect(l1, r1, l2, r2)
    if inters < 1:
        return 0
    elif k >= left and k <= right:
        return inters - 1
    else:
        return inters


def __starting_point():
    ans = solve()
    print(ans)


__starting_point()
