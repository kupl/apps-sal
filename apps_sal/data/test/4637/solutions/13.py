# int(input())
# [int(s) for s in input().split()]
# input()


def solve():
    t = int(input())

    for i in range(t):
        n, k = [int(s) for s in input().split()]
        a = sorted([int(s) for s in input().split()])
        b = sorted([int(s) for s in input().split()], reverse=True)

        for j in range(k):
            if a[j] <= b[j]:
                a[j] = b[j]

        print(sum(a))


def __starting_point():
    solve()
__starting_point()
