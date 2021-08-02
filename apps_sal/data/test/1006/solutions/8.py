n = int(input())
s = [list(input()) for _ in range(n)]


def TryCross(i, j):
    if 0 <= i < n - 2 and 0 < j < n - 1:
        c = [(i, j), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1), (i + 2, j)]
        if not all(s[x][y] == "#" for x, y in c):
            return False
        for x, y in c:
            s[x][y] = "."
        return True
    return False


for i in range(n):
    for j in range(n):
        if s[i][j] == "#" and not TryCross(i, j):
            print("NO")
            return
print("YES")
