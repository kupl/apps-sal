n = int(input())
m = list()
for i in range(n):
    m.append(list((int(x) for x in input().split())))
c = 0
for i in range(n):
    if m[i][0] + 2 <= m[i][1]:
        c += 1
print(c)
