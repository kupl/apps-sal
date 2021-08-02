n = int(input())
m = [input() for s in range(n)]

count = 0

for i in range(1, n - 1):
    for j in range(1, n - 1):
        if m[i][j] == m[i - 1][j - 1] == m[i - 1][j + 1] == m[i + 1][j + 1] == m[i + 1][j - 1] == 'X':
            count += 1

print(count)


def __starting_point():
    pass


__starting_point()
