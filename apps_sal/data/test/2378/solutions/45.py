import sys
input = sys.stdin.readline

mod = 10**9 + 7


def dfs(graph, N):
    ans = 0
    Par = [-1] * N
    Childs = [[] for _ in range(N)]
    stack = [0]
    while stack:
        p = stack.pop()
        if p >= 0:
            stack.append(~p)
            for np in graph[p]:
                if np != 0 and Par[np] == -1:
                    stack.append(np)
                    Par[np] = p
        else:
            p = ~p
            score = pow(2, N - 1, mod) - 1
            upper = N - 1
            for a in Childs[p]:
                upper -= a
                score = (score - pow(2, a, mod) + 1) % mod
            if p != 0:
                score = (score - pow(2, upper, mod) + 1) % mod
            ans = (ans + score) % mod
            Childs[Par[p]].append(N - 1 - upper + 1)

    return ans * pow(2, N * (mod - 2), mod) % mod


def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list(map(int, input().split()))
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    print((dfs(graph, N)))


def __starting_point():
    main()


__starting_point()
