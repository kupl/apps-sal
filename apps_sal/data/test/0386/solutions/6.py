n = int(input())
k = 0
a = []
r = []
h = 0
for i in range(n):
    a.append(list(map(str, input().split())))
for i in range(n):
    for j in range(1):
        if a[i][j] == '>=' and a[i][j + 2] == 'Y':
            if k < int(a[i][j + 1]):
                k = int(a[i][j + 1])
        if a[i][j] == '>=' and a[i][j + 2] == 'N':
            if k >= int(a[i][j + 1]):
                k = int(a[i][j + 1]) - 1
        if a[i][j] == '>' and a[i][j + 2] == 'Y':
            if k <= int(a[i][j + 1]):
                k = int(a[i][j + 1]) + 1
        if a[i][j] == '>' and a[i][j + 2] == 'N':
            if k > int(a[i][j + 1]):
                k = int(a[i][j + 1])
        if a[i][j] == '<=' and a[i][j + 2] == 'Y':
            if k > int(a[i][j + 1]):
                k = int(a[i][j + 1])
        if a[i][j] == '<=' and a[i][j + 2] == 'N':
            if k <= int(a[i][j + 1]):
                k = int(a[i][j + 1]) + 1
        if a[i][j] == '<' and a[i][j + 2] == 'Y':
            if k >= int(a[i][j + 1]):
                k = int(a[i][j + 1]) - 1
        if a[i][j] == '<' and a[i][j + 2] == 'N':
            if k < int(a[i][j + 1]):
                k = int(a[i][j + 1])
for i in range(n):
    for j in range(1):
        if a[i][j] == '>=' and a[i][j + 2] == 'Y':
            if k >= int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '>=' and a[i][j + 2] == 'N':
            if k < int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '>' and a[i][j + 2] == 'Y':
            if k > int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '>' and a[i][j + 2] == 'N':
            if k <= int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '<=' and a[i][j + 2] == 'Y':
            if k <= int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '<=' and a[i][j + 2] == 'N':
            if k > int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '<' and a[i][j + 2] == 'Y':
            if k < int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
        if a[i][j] == '<' and a[i][j + 2] == 'N':
            if k >= int(a[i][j + 1]):
                r.append('+')
            else:
                r.append('-')
for i in range(len(r)):
    if r[i] == '-':
        print('Impossible')
        h = 0
        break
    else:
        h += 1
if h != 0:
    print(k)
