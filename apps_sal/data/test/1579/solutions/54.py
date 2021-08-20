import sys
sys.setrecursionlimit(10 ** 6)


def main():
    input = sys.stdin.readline
    V = 10 ** 5
    N = int(input())
    bgraph = [[] for _ in range(2 * V)]
    for _ in range(N):
        (x, y) = list(map(int, input().split()))
        x -= 1
        y += V - 1
        bgraph[x].append(y)
        bgraph[y].append(x)

    def dfs(i):
        if visited[i]:
            return cnt
        visited[i] = True
        cnt[i // V] += 1
        for j in bgraph[i]:
            dfs(j)
        return cnt
    visited = [False] * (2 * V)
    ans = 0
    for i in range(V):
        if visited[i]:
            continue
        cnt = [0, 0]
        cnt = dfs(i)
        ans += cnt[0] * cnt[1]
    ans -= N
    return ans


def __starting_point():
    print(main())


__starting_point()
