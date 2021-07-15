import string


def main():
    n, m = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    sm = 0
    for i in lst:
        sm += i
    print(min(sm, m))


def __starting_point():
    t = int(input())
    for i in range(t):
        main()

__starting_point()
