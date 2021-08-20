n = int(input())
c = list(input())
rcnt = 0
allrcnt = 0
for i in range(len(c)):
    if c[i] == 'R':
        allrcnt += 1
for i in range(len(c)):
    if i + 1 <= allrcnt and c[i] == 'R':
        rcnt += 1
ans = allrcnt - rcnt
print(ans)
