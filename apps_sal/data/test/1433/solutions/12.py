n, m = list(map(int, input().split()))

jadval = []
for i in range(n):
    jadval.append(list(input().replace(" ", "")))
s = 0
for i in range(n):
    f = 0
    for j in range(m):
        if jadval[i][j] == '1':
            f = 1
        elif f == 1:
            s += 1
for i in range(n):
    f = 0
    j = m - 1
    while j >= 0:
        if jadval[i][j] == '1':
            f = 1
        elif f == 1:
            s += 1
        j -= 1
for j in range(m):
    f = 0
    for i in range(n):
        if jadval[i][j] == '1':
            f = 1
        elif f == 1:
            s += 1
for j in range(m):
    f = 0
    i = n - 1
    while i >= 0:
        if jadval[i][j] == '1':
            f = 1
        elif f == 1:
            s += 1
        i -= 1
print(s)
