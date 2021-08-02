def main():
    def dfs(t):
        pos.append(t)
        unused[t] = False
        for k, (a, u) in enumerate(zip(A[t], unused)):
            if a and u:
                dfs(k)

    n = int(input())
    pp = list(map(int, input().split()))
    A = [list(map(int, input())) for _ in range(n)]
    unused = [True] * n
    for i, f in enumerate(unused):
        if f:
            pos = []
            dfs(i)
            for j, v in zip(sorted(pos), sorted(pp[_] for _ in pos)):
                pp[j] = v
    print(' '.join(map(str, pp)))


def __starting_point():
    main()


__starting_point()
