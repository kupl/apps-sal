def read_data():
    n, m = list(map(int, input().strip().split()))
    a = []
    for i in range(n):
        line = list(input().strip())
        for j in range(len(line)):
            if line[j] == ".":
                line[j] = 0
            else:
                line[j] = 1
        a.append(line)
    return n, m, a

def get_step(i,j):
    rows = []
    cols = []
    for k in range(m):
        if a[i][k] == 1:
            cols.append(k)
            if k in usedc:
                return "No"
            else:
                usedc.append(k)
    for k in range(n):
        if a[k][j] == 1:
            rows.append(k)
            if k in usedr:
                return "No"
            else:
                usedr.append(k)
    for row in rows:
        for col in cols:
            if a[row][col] == 0:
                return "No"
            else:
                a[row][col] = 0
    return "Ok"

def solve():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                step = get_step(i,j)
                if step == "No":
                    return "No"
    return "Yes"

n, m, a = read_data()
usedr = []
usedc = []
print(solve())

