a, b, c = map(int, input().split(' '))
array = [[i for i in input()] for j in range(a)]
p = []
x = 0
for i in range(a):
    for j in range(b):
        if array[i][j] == '.':
            p = [(i, j)]
            x += 1

visited = [[False for _ in range(b)] for i in range(a)]


def ok(i, j):
    if 0 <= i <= a - 1 and 0 <= j <= b - 1:
        if array[i][j] == '.':
            return True
    return False


sa = 0
while sa < x - c:
    i, j = p[-1]
    p.pop()
    if not visited[i][j]:
        if ok(i, j - 1):
            if not visited[i][j - 1]:
                p.append((i, j - 1))
        if ok(i, j + 1):
            if not visited[i][j + 1]:
                p.append((i, j + 1))
        if ok(i + 1, j):
            if not visited[i + 1][j]:
                p.append((i + 1, j))
        if ok(i - 1, j):
            if not visited[i - 1][j]:
                p.append((i - 1, j))
        visited[i][j] = True
        sa += 1

for i in range(a):
    for j in range(b):
        if array[i][j] == '.' and not visited[i][j]:
            array[i][j] = 'X'

for each in [''.join(i) for i in array]:
    print(each)
