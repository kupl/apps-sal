def solve(x, y):
    if (x == y):
        return '='
    if 2 in [x, y] and 4 in [x, y]:
        return '='
    if x == 1:
        return '<'
    if y == 1:
        return '>'
    if x == 3 and y == 2:
        return '>'
    if x == 2 and y == 3:
        return '<'
    if x < y:
        return '>'
    return '<'

x, y = list(map(int, input().split()))
print(solve(x, y))
