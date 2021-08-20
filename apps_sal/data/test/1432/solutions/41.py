def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = []
    x1 = 0
    for (i, ai) in enumerate(A):
        x1 += ai if i % 2 == 0 else -ai
    x1 //= 2
    ans.append(x1)
    for a in A[:-1]:
        ans.append(a - ans[-1])
    print(' '.join((str(a * 2) for a in ans)))


def __starting_point():
    main()


__starting_point()
