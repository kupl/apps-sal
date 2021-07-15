s = str(input())
tmp = {}
for i in range(4):
    tmp.setdefault(s[i],0)
    tmp[s[i]]+=1
if len(tmp)==2 and max(tmp.values())==2:
    print('Yes')
else:
    print('No')
