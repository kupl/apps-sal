import sys


def main():
    x = sys.stdin.readline().split()

    l = int(x[0])
    r = int(x[1])
    xx = int(x[2])
    y = int(x[3])
    k = int(x[4])
    for i in range(xx, y + 1):
        p = i * k
        if l <= p and p <= r:
            print("YES")
            return
    print("NO")


def __starting_point():
    main()


__starting_point()
