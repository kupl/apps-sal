a, b, c = list(map(int, input().split(' ')))


def solve(a, b, c):
    if b >= c:
        b, c = c, b
    for i in range(max(6 * a, b * c), 10**50):
        for j in range(b, int(i**0.5) + 1):
            if i % j == 0:
                if int(i / j) >= c:
                    return (i, j, int(i / j))


x, y, z = solve(a, b, c)

print(x)
if y >= b and z >= c:
    print(y, z)
else:
    print(z, y)
