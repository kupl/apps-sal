from itertools import product, accumulate
import sys
sys.stdin.readline

def main():
    N, W = map(int, input().split())
    V = [[] for _ in range(4)]
    w1 = 0
    for i in range(N):
        w, v = map(int, input().split())
        if i == 0: w1 = w
        V[w-w1].append(v)
    U = []
    for i in range(4):
        U.append([0] + list(accumulate(sorted(V[i], reverse=True))))

    ans = 0
    for prod in product(*[range(len(U[i])) for i in range(4)]):
        if sum((i+w1)*p for i, p in enumerate(prod)) <= W:
            ans = max(ans, sum(U[i][p] for i, p in enumerate(prod)))
    print(ans)

def __starting_point():
    main()
__starting_point()
