def solve(x, y, z):
    x, y, z = sorted([x, y, z])
    if x == y == z:
        return [x, x, x]
    elif x < y and y == z:
        return [x, x, z]
    return None

t = int(input())
for _ in range(t):
    # n = int(input())
    x, y, z = map(int, input().split())
    # c = list(map(int, input().split()))
    sol = solve(x, y, z)
    if sol:
        print('YES')
        print(' '.join(map(str, sol)))
    else:
        print('NO')
