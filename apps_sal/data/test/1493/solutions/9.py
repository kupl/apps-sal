n, m = map(int, input().split())
table = []
for i in range(n//2):
    table += [["B", "W"] * (m//2) + ["B"] * (m%2), ["W", "B"] * (m//2) + ["W"] * (m%2)]
table += [["B", "W"] * (m//2) + ["B"] * (m%2)] * (n%2)
for i in range(n):
    s = list(input().strip())
    for j in range(m):
        if s[j] == '-':
            table[i][j] = '-'
print('\n'.join(list(map(''.join, table))))
