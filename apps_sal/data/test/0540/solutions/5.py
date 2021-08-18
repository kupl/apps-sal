row, col = (int(x) for x in input().split())

matrix = [['X' for i in range(col + 2)]]
for _ in range(row):
    matrix.append(['X'] + [str(x) for x in input()] + ['X'])
matrix.append(['X' for i in range(col + 2)])

startR, startC = (int(x) for x in input().split())
endR, endC = (int(x) for x in input().split())


def search_way(matrix, startR, startC, endR, endC):
    countToEnd = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(len(dx)):
        if matrix[endR + dx[i]][endC + dy[i]] == '.':
            countToEnd += 1
    if endR == startR and endC == startC:
        if matrix[endR][endC] == 'X' and countToEnd < 1:
            return "NO"
        elif matrix[endR][endC] == 'X':
            return "YES"

    if countToEnd < 2 and matrix[endR][endC] == '.':
        if countToEnd == 1 and abs(endR - startR) + abs(endC - startC) == 1:
            return "YES"
        return "NO"
    matrix[endR][endC] = '.'
    queue = [(startR, startC), ]
    while len(queue) >= 1:
        curValue = queue.pop(-1)
        if curValue[0] == endR and curValue[1] == endC:
            return "YES"
        for i in range(len(dx)):
            if matrix[curValue[0] + dx[i]][curValue[1] + dy[i]] == '.':
                matrix[curValue[0] + dx[i]][curValue[1] + dy[i]] = 'X'
                queue.append((curValue[0] + dx[i], curValue[1] + dy[i]))
    return "NO"


print(search_way(matrix, startR, startC, endR, endC))
