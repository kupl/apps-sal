import sys


def main():
    x = 1234567
    y = 123456
    z = 1234
    s = int(sys.stdin.readline())
    if s % x == 0:
        print("YES")
        return

    while s > 0:
        if s % y == 0:
            print("YES")
            return
        s1 = s
        while s1 > 0:
            if s1 % z == 0:
                print("YES")
                return
            s1 -= y
        s -= x

    print("NO")


main()
