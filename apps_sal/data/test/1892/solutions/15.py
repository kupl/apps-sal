def add(x, j):
    x = x % (1000000000 + 7)
    j = j % (1000000000 + 7)
    return (x + j) % (1000000000 + 7)


statements = []
n = int(input())
i = 1
j = 1
temp = [[0 for i in range(n)] for i in range(n)]
earlier = [[0 for i in range(n)] for i in range(n)]
temp[0][0] = 1
earlier[0][0] = 1

while(i <= n):
    s = input()
    statements.append(s)
    i += 1
while(j < n):
    temp[0][j] = 0
    earlier[0][j] = temp[0][j] + earlier[0][j - 1]
    j += 1
i = 1
while(i < n):
    if(statements[i - 1] == 'f'):
        j = 1
        while(j < n):
            temp[i][0] = 0
            earlier[i][0] = 0
            temp[i][j] = temp[i - 1][j - 1]
            earlier[i][j] = add(earlier[i][j - 1], temp[i][j])

            j += 1
    else:
        j = 0
        while(j < n):
            if(j == 0):
                temp[i][j] = earlier[i - 1][n - 1]
            else:
                temp[i][j] = earlier[i - 1][n - 1] - earlier[i - 1][j - 1]
            earlier[i][j] = add(earlier[i][j - 1], temp[i][j])
            j += 1
    i += 1

ans = 0
j = 0
while(j < n):
    ans = add(ans, temp[n - 1][j])
    j += 1

print(ans % (1000000000 + 7))
