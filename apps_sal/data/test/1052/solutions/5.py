import sys


def main():
    args = sys.stdin.readline()[:-1].split()
    (n, k) = (int(args[0]), int(args[1]))
    a = 1
    b = n * (n - 1) // 2
    c = n * (n - 1) * (n - 2) // 6 * 2
    d = n * (n - 1) * (n - 2) * (n - 3) // 24 * 9
    if k == 1:
        print(a)
    if k == 2:
        print(a + b)
    if k == 3:
        print(a + b + c)
    if k == 4:
        print(a + b + c + d)


main()
