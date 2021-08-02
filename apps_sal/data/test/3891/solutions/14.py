3

n, m = list(map(int, input().split()))

s = [input() for i in range(n)]
ts = [[s[i][j] for i in range(n)] for j in range(m)]

has_b_row = [i for i in range(n) if 'B' in s[i]]
has_b_column = [j for j in range(m) if 'B' in ts[j]]

print(has_b_row[len(has_b_row) // 2] + 1, has_b_column[len(has_b_column) // 2] + 1)
