def solve(x, y):
    if x < 0:
        x, y = solve(-x, y)
        return -x, y
    if y < 0:
        x, y = solve(x, -y)
        return x, -y
    if x > y:
        x, y = solve(y, x)
        return y, x

    if x + y >= 2 * K:
        return x, y - K
    if x + y == K:
        return 0, 0

    r = K - (x + y) // 2
    return -r, (x + y + r - K)


K, X, Y = map(int, open(0).read().split())

if K % 2 == 0 and (X + Y) % 2 == 1:
    print(-1)
    return

A = []
while X or Y:
    A.append((X, Y))
    X, Y = solve(X, Y)

print(len(A))
for a in reversed(A):
    print(*a)
