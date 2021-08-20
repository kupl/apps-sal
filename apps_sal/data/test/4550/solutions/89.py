import sys
sys.setrecursionlimit(250000)


def main():
    (a, b, c) = list(map(int, input().split()))
    if a == b + c:
        print('Yes')
    elif b == a + c:
        print('Yes')
    elif c == a + b:
        print('Yes')
    else:
        print('No')


main()
