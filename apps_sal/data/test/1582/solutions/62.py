def solve():
    table = [[0] * 10 for _ in range(10)]
    for i in range(N + 1):
        s = list(map(int, str(i)))
        table[s[0]][s[-1]] += 1
    return sum(table[i][j] * table[j][i] for i in range(1, 10) for j in range(1, 10))


N = int(input())
print((solve()))

