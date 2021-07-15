n, m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = []
for i in range(m):
    b.append(list(map(int,input().split())))
ans = -1000000000

for i in range(n):
    ac = a.copy()
    for j in range(m):
        if i+1 < b[j][0] or i+1 > b[j][1]:
            for k in range(b[j][0]-1, b[j][1]):
                ac[k] -= 1
    if a[i] - min(ac) > ans:
        ans = a[i] - min(ac)
        ansi = i

ansh = []
i = ansi
ac = a.copy()
q = 0
for j in range(m):
    if i+1 < b[j][0] or i+1 > b[j][1]:
        q += 1
        ansh.append(j+1)

print(ans)
print(q)
print(*ansh)


