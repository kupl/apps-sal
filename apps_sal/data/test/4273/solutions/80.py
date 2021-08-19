import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    D = dict()
    W = ['M', 'A', 'R', 'C', 'H']
    for w in W:
        D[w] = 0
    for _ in range(N):
        S = input().strip('\n')
        if S[0] in W:
            D[S[0]] += 1
    ans = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                ans += D[W[i]] * D[W[j]] * D[W[k]]
    print(ans)
    return 0


def __starting_point():
    solve()


__starting_point()
