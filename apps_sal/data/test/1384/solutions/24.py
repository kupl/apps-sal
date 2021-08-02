n = int(input())
p = list(map(int, input().split()))
ind_z = []
ind_o = []
for i in range(n):
    if p[i] == 0:
        ind_z.append(i)
    else:
        ind_o.append(i)
z = [0] * len(ind_z)
o = [0] * len(ind_o)
for i in range(len(z)):
    z[i] = i + 1
    for j in range(ind_z[i], n):
        if p[j] == 1:
            z[i] += 1
for i in range(len(o)):
    o[i] = len(o) - i
    for j in range(ind_o[i] - 1, -1, -1):
        if p[j] == 0:
            o[i] += 1
z = [0] + z
o = [0] + o
print(max(max(o), max(z)))
