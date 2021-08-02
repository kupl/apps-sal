def solve():
    N = int(input())
    Ass = [tuple([int(x) - 1 for x in input().split()]) for _ in range(N)]

    day = 0
    numMatch = 0
    ps = set(range(N))
    isReadys = [0] * N
    iAs = [-1] * N
    while True:
        day += 1
        p2s = set()
        for p in ps:
            iAs[p] += 1
            if iAs[p] == N - 1:
                continue
            q = Ass[p][iAs[p]]
            if isReadys[q] and Ass[q][iAs[q]] == p:
                isReadys[q] = 0
                p2s.add(p)
                p2s.add(q)
                numMatch += 1
            else:
                isReadys[p] = 1
        if numMatch >= N * (N - 1) // 2:
            print(day)
            break
        if not p2s:
            print((-1))
            break
        ps = p2s


solve()
