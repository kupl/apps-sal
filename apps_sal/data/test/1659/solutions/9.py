import sys


def main():
    x = sys.stdin.readline().split()
    n, x = int(x[0]), int(x[1])
    g = 0
    for i in range(n):
        y = sys.stdin.readline().split()
        k = int(y[1])
        if y[0] == '-':
            if k > x:
                g += 1
            else:
                x -= k
        else:
            x += k
    print(x, g)


main()
