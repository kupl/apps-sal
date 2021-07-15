LI = lambda: list(map(int, input().split()))

N, M = LI()
S, C = [None] * M, [None] * M
for i in range(M):
    S[i], C[i] = LI()


def main():
    l = [None] * N
    for s, c in zip(S, C):
        if l[s - 1] is None:
            l[s - 1] = c
        elif l[s - 1] != c:
            print((-1))
            return
    
    if N > 1 and l[0] == 0:
        print((-1))
        return
    if l[0] is None:
        l[0] = 0 if N == 1 else 1
    for i in range(1, N):
        if l[i] is None:
            l[i] = 0
    
    ans = "".join(list(map(str, l)))
    print(ans)


def __starting_point():
    main()

__starting_point()
