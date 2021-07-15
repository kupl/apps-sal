a = int(input())
sa = []
for i in range(a):
    x, y = map(str, input().split(' '))
    sa.append([x, y, 0])
for i in sa:
    if i[2] == 0:
        for j in sa:

            if j[2] == 0 and i[1] == j[0]:
                i[1] = j[1]
                j[2] = 2
        i[2] = 1
a = [i for i in sa if i[2] == 1]
print(len(a))
for i in a:
    print(i[0], i[1])
