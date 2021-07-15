n, S = map(str, input().rstrip().split(" "))

n = int(n)
S = list(S)
cnt = 0

ac = 0
cg = 0

def nC2(num):
    ret = num * (num - 1) // 2
    return ret

Sum = []
for i, s in enumerate(S):
    if(s == "A"):
        ac += 1
    elif(s == "T"):
        ac -= 1
    elif(s == "C"):
        cg += 1
    elif(s == "G"):
        cg -= 1
    
    Sum.append((ac, cg))

cnt = 0
Table = {}
for t in Sum:
    if(t == (0, 0)):
        cnt += 1
        
    if(t in Table):
        Table[t] += 1
    else:
        Table[t] = 1

for table in Table:
    tmp = Table[table]
    tmp = nC2(tmp)
    cnt += tmp
print(cnt)
