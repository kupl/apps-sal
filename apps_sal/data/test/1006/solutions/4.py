import sys

n = int(sys.stdin.readline())
lines = []
for i in range(n):
    lines.append(list(sys.stdin.readline().strip()))


def check(lines, x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if lines[x][y] != '#':
        return False
    lines[x][y] = '.'
    return True


def tryPaint(lines, i, j, n):
    return check(lines, i, j, n) and \
        check(lines, i - 1, j + 1, n) and \
        check(lines, i, j + 1, n) and \
        check(lines, i + 1, j + 1, n) and \
        check(lines, i, j + 2, n)


failed = False

for j in range(n):
    for i in range(n):
        if lines[i][j] == '#':
            if not tryPaint(lines, i, j, n):
                failed = True
                break
        if failed:
            break

if not failed:
    for i in range(n):
        if "#" in set(lines[i]):
            failed = True
            break

if failed:
    print("NO")
else:
    print("YES")
