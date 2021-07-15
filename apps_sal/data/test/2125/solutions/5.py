n,m = [int(i) for i in input().split()]
data = []
for i in range(n):
    data.append(list(input()))
#print(data)
f = []
for i in range(m):
    
    temp = []
    prev = 0
    cnt = 0 #-1?????
    for j in range(n):
        ch = ord(data[j][i]) - 95
        if ch == prev:
            cnt += 1
        else:
            temp.append((prev, cnt, j - cnt))
            prev = ch
            cnt = 1
    temp.append((prev, cnt, n - cnt))
    for t in range(1, len(temp)-1):
        td = temp[t-1]
        tf = temp[t+1]
        te = temp[t]
        if te[0] != td[0] and te[0] != tf[0] and td[1] >= te[1] and tf[1] >= te[1]:
            f.append((te[2],i, te[1], (td[0]<<10) + (te[0]<<5)+tf[0]))

tot = 0
f.sort()
#print(f)

le = len(f)
i = 0
while i < le:
    d = f[i]
    cnt = 1
    #print(d, f[i+1])
    while i < le -1  and d[1] + cnt == f[i+1][1] and d[0] == f[i+1][0] and  d[2] == f[i+1][2] and d[3] == f[i+1][3]:
        i+=1
        cnt+=1
    #print(cnt)
    tot += (cnt*(cnt+1))//2
    i += 1

print(tot)
    

