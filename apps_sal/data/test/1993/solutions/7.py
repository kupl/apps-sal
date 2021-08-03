from sys import stdin, stdout


def st(): return list(stdin.readline().strip())
def li(): return list(map(int, stdin.readline().split()))
def mp(): return list(map(int, stdin.readline().split()))
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n) + "\n")


def valid(x, y):
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    if v[x][y] or l[x][y] == '*':
        return False
    return True


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(i, j, val):
    ans = 1
    connected = [(i, j)]
    stack = [(i, j)]
    v[i][j] = True
    while stack:
        a, b = stack.pop()
        for x in range(4):
            newX, newY = a + dx[x], b + dy[x]
            if valid(newX, newY):
                stack.append((newX, newY))
                v[newX][newY] = True
                connected.append((newX, newY))
                ans = ans + 1

    for i in connected:
        a, b = i
        l[a][b] = (ans, val)


n, m = mp()
l = [st() for i in range(n)]
val = 0
k = [list(i) for i in l]
v = [[False for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if l[i][j] == '.' and not v[i][j]:
            DFS(i, j, val)
            val += 1

for i in range(n):
    for j in range(m):
        if l[i][j] == '*':
            k[i][j] = 1
            s = set()
            for x in range(4):
                newX, newY = i + dx[x], j + dy[x]
                if 0 <= newX < n and 0 <= newY < m:
                    if type(l[newX][newY]) == tuple:
                        A, B = l[newX][newY]
                        if B not in s:
                            k[i][j] += A
                            k[i][j] %= 10
                            s.add(B)


print('\n'.join([''.join([str(i) for i in j]) for j in k]))
