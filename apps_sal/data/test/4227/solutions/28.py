import copy


def dfs(i, path, reached, n):
    if reached[i]:
        return n
    reached[i] = True
    if all(reached):
        n += 1
        return n
    for p in path[i]:
        org_reached = copy.deepcopy(reached)
        n = dfs(p, path, org_reached, n)
    return n


def main():
    (N, M) = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    path = [[] for _ in range(N)]
    for (a, b) in AB:
        a -= 1
        b -= 1
        path[a].append(b)
        path[b].append(a)
    reached = [False for _ in range(N)]
    n = 0
    n = dfs(0, path, reached, n)
    print(n)


main()
