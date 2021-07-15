def lexyco(table, pos):
    for i in range(len(table)-1):
        for s2 in table[i+1:]:
            if (table[i][:pos+1] > s2[:pos+1]):
                return False
    return True

n, m = map(int, input().split())
table = []
for i in range(n):
    table.append(input())
cnt = 0
i = 0
while i < len(table[0]):
    if lexyco(table, i):
        i += 1
    else:
        cnt += 1
        for s in range(len(table)):
            table[s] = table[s][:i] + table[s][i+1:]
print(cnt)
