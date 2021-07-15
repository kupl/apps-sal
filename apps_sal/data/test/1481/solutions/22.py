def prepare(n):
    table = [[0] * n for _ in range(n)]
    
    for i in range(n):
        line = input()
        for j in range(n):
            if line[j] == 'o':
                if i - 1 >= 0:
                    table[i - 1][j] = (table[i - 1][j] + 1) % 2
                    if table[i - 1][j] != 0:
                        return 'NO'
                if j - 1 >= 0:
                    table[i][j - 1] = (table[i][j - 1] + 1) % 2
                if j + 1 < n:
                    table[i][j + 1] = (table[i][j + 1] + 1) % 2
                if i + 1 < n:
                    table[i + 1][j] = (table[i + 1][j] + 1) % 2
    for j in range(n):
        if table[n - 1][j] != 0:
            return 'NO'
    return 'YES'


def __starting_point():
    n = int(input())
    
    print(prepare(n))


__starting_point()
