n, m = [int(i) for i in input().split()]
field = []
for i in range(n):
    field.append(input().strip())
st_i = -1
st_j = -1
en_i = -1
en_j = -1
result = "YES"
top_left_found = False
for i in range(n):
    for j in range(m):
        if not top_left_found and field[i][j] == 'X':
            top_left_found = True
            st_i = i
            st_j = j
            for k in range(i, n):
                if not 'X' in field[k] and en_i == -1:
                    en_i = k - 1;
            if en_i == -1:
                en_i = n - 1
        elif top_left_found:
            if i != st_i and en_j == -1:
                en_j = m - 1;
            if field[i][j] == '.' and i == st_i and en_j == -1:
                en_j = j - 1;
            elif en_j != -1 and field[i][j] == 'X' and ((j < st_j) or (j > en_j) or (i < st_i) or (i > en_i)):
                result = "NO"
            elif en_j != -1 and field[i][j] == '.' and ((st_j <= j <= en_j) and (st_i <= i <= en_i)):
                result = "NO"
print(result)
