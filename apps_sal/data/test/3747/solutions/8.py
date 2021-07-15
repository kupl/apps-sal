d={'B':0,'u':0,'l':0,'b':0,'a':0,'s':0,'a':0,'u':0,'r':0}
for x in input():
    if x in d: d[x]+=1
d['a']//=2; d['u']//=2
print(min(d.values()))
