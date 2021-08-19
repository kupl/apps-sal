def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = list(reversed(p))
    for i in p:
        print(i, end=' ')
    print()


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


'\n60, 61\n'
'\n'
__starting_point()
