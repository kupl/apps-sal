import sys
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())


def __starting_point():

    n = ii()
    a = lmi()
    if all([i % 2 == 0 for i in a]) or all([i % 2 == 1 for i in a]):
        for i in a:
            print(i, end=" ")
        print()
    else:
        a.sort()
        for i in a:
            print(i, end=" ")
        print()


__starting_point()
