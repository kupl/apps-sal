def transpose(x):
    return [list(row) for row in zip(*x)]

def canpurify(x):
    for i in x:
        founddot = False
        for j in i:
            if j == '.':
                founddot = True
                break
        if not founddot:
            return False
    return True

field = []
n = int(input())

def purify(x, transposed):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j] == '.':
                if not transposed:
                    print(i+1, j+1)
                else:
                    print(j+1, i+1)
                break

for _ in range(n):
    field.append(input())
t = False
if not canpurify(field):
    field = transpose(field)
    t = True

if canpurify(field):
    purify(field, t)
else:
    print(-1)


