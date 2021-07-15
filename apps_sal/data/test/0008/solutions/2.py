m={"s":[0]*9, "m":[0]*9, "p":[0]*9}
for e in input().split():
    m[e[1]][int(e[0])-1]+=1
ret=2
for t in "smp":
    l=m[t]
    if max(l)>=2:
        ret=min(ret, 3-max(l))
    else:
        for i in range(7):
            seq = sum(l[i:i+3])
            ret = min(ret, 3-seq)
print(ret)
