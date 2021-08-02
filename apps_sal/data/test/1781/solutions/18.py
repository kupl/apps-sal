n, z = map(int, input().split())
s = 0
a = []
x = []
for j in range(n):
    c = list(input())
    x.append(c)
    for i in range(12):
        if c[i] == '.':
            if i == 0:
                if c[1] == 'S':
                    a.append([1, (j, 0)])
                else:
                    a.append([0, (j, 0)])
            elif i == 11:
                if c[10] == 'S':
                    a.append([1, (j, 11)])
                else:
                    a.append([0, (j, 11)])
            else:
                k = 0
                if c[i - 1] == 'S':
                    k += 1
                if c[i + 1] == 'S':
                    k += 1
                a.append([k, (j, i)])
        if c[i] == 'S':
            if i == 0:
                if c[1] not in '.-':
                    s += 1
            elif i == 11:
                if c[10] not in '.-':
                    s += 1
            else:
                if c[i - 1] not in '.-':
                    s += 1
                if c[i + 1] not in '.-':
                    s += 1
a.sort()
b = []
c = []
for i in range(z):
    b.append(a[i][0])
    c.append(a[i][1])
for i in range(z):
    x[c[i][0]][c[i][1]] = 'x'
print(s + sum(b))
for i in range(n):
    print(''.join(x[i]))
