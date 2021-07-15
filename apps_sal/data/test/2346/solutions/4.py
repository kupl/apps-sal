n = int(input())
lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))
    
x = list([0]*n)
p = list([0]*n)

res = []
for i in lis:
    if i[0] != -1:
        p[i[0]-1] += (i[-1])
        x[i[0]-1] += 1    
for i in range(n):
    if lis[i][-1] == 1:
        if x[i] == p[i]:
            res.append(i+1)

if len(res) == 0:
    print(-1)
else:
    print(" ".join(map(str, sorted(res))))

