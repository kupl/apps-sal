import collections


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A1 = []
    A2 = []
    for (i, a) in enumerate(A):
        A1.append(i + 1 + a)
        A2.append(i + 1 - a)
    A1count = list(collections.Counter(A1).items())
    A2count = collections.Counter(A2)
    ans = 0
    for (a, cnt) in A1count:
        ans += A2count[a] * cnt
    print(ans)


def __starting_point():
    main()


__starting_point()
