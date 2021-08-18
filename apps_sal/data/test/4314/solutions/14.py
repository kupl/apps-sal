h, w = map(int, input().split())
a = []

for i in range(h):
    r = list(input())
    if '
    a.append(r)

box = [0] * w

for colum in range(w):
    if all(row[colum] == '.' for row in a):
        box[colum] = 1

for j in range(w):
    if box[j] == 1:
        for row in a:
            row[j] = ''

for row in a:
    print(''.join(map(str, row)))
