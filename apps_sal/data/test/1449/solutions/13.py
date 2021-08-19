import sys
# sys.stdin = open("input.txt")


def main():
    T = int(input())
    for ti in range(T):
        n, k = list(map(int, input().split()))
        A = set(int(v) for v in input().split())
        if k == 1:
            if len(A) == 1:
                print(1)
            else:
                print(-1)
            continue
        if len(A) == 1:
            print(1)
        else:
            print((len(A) - 3 + k) // (k - 1))


def __starting_point():
    main()


__starting_point()
