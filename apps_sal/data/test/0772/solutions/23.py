s = [[1] * 5 for _ in range(5)]
for i in 1, 2, 3:
    for j, v in zip((1, 2, 3), map(int, input().split())):
        for k, d in (-1, 0), (1, 0), (0, -1), (0, 1), (0, 0):
            s[i + k][j + d] += v
for i in 1, 2, 3:
    for j in 1, 2, 3:
        print(s[i][j] % 2, end='')
    print()
