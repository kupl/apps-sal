N, X = list(map(int, input().split(' ')))

p = [1]
pb = [1]
np = 0
nx = X

for _ in range(N):
    p.append(p[-1] * 2 + 1)
    pb.append(pb[-1] * 2 + 3)


def dfs(level):
    nonlocal np, nx

    if nx == 0:
        return

    if nx >= pb[level]:
        nx -= pb[level]
        np += p[level]
        return

    nx -= 1
    if nx == 0:
        return

    dfs(level - 1)

    if nx == 0:
        return

    nx -= 1
    np += 1

    if nx == 0:
        return

    dfs(level - 1)

    if nx == 0:
        return

    nx -= 1


dfs(N)

print(np)

