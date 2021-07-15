k = int(input())

a = [['' for _ in range(2 ** k)] for _ in range(2 ** k)]
a[0][0] = '+'

for m in range(1, k+1):
    p = 2 ** (m - 1)
    for i in range(p):
        for j in range(p):
            a[p+i][j] = a[i][j]
            if i % 2 == 0:
                a[i][p+j] = '*' if a[i][j] == '+' else '+'
                a[p+i][p+j] = a[i][j]
            else:
                a[i][p+j] = a[i][j]
                a[p+i][p+j] = '*' if a[i][j] == '+' else '+'

print('\n'.join(''.join(x) for x in a))
