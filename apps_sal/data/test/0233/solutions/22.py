import sys


def main():

    n = int(sys.stdin.readline())
    m, c = 0, 0
    for i in range(n):
        x = sys.stdin.readline().split()

        a, b = int(x[0]), int(x[1])
        if a > b:
            m += 1
        elif a < b:
            c += 1
    if m > c:
        print("Mishka")
    elif m < c:
        print("Chris")
    else:
        print("Friendship is magic!^^")


main()
