n=int(input())
p = [[1], [0, 1]]
for i in range(n-1):
    t=[0]+p[-1]
    for j in range(len(p[i])):
        t[j]^=p[i][j]
    p.append(t)
print(n)
print(*p[n])
print(n-1)
print(*p[-2])

