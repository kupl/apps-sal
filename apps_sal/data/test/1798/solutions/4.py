n = int(input())
A = [int(i) for i in input().split()]

table = [None for i in range(100001)]

for i, x in enumerate(A):
    if table[x] == None:
        table[x] = [i, 0]
    else:
        previ = table[x][0]
        if previ == -1:
            continue
        prevp = table[x][1]
        if prevp == 0:
            table[x][0] = i
            table[x][1] = i - previ
        else:
            currentp = i - previ
            if currentp == prevp:
                table[x][0] = i
            else:
                table[x][0] = -1

output = [(x, t[1]) for x, t in enumerate(table) if t != None and t[0] != -1]
s = str(len(output)) + '\n'
for x, p in output:
    s += str(x) + ' ' + str(p) + '\n'
print(s)
