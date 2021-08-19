q = str(input())
pr = 0
suf = 0
for i in range(1, len(q)):
    if q[i] == '0':
        pr *= 10
    suf += pr
    pr = int(q[i])
suf += pr
print(suf + 1)
