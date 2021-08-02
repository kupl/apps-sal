N, M = list(map(int, input().split()))
A = [[] for i in range(N)]

for i in range(M):
    x, y = list(map(int, input().split()))
    A[x - 1].append(y)
    A[y - 1].append(x)

color = ["W" for i in range(N)]

clear = ["B" for i in range(N)]


def path(x, d):
    if color[x - 1] == "B":
        return False

    color[x - 1] = "B"

    if color == clear:
        color[x - 1] = "W"
        return True

    ans = 0
    for i in range(len(A[x - 1])):
        ans += int(path(A[x - 1][i], d + 1))

    color[x - 1] = "W"
    return ans


print((path(1, 0)))
