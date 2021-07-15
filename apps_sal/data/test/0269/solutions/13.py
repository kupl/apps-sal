s=input()
col=['R','B','Y','G']
p=[0]*4
sootv=[0]*4
for i in range(len(s)):
    if s[i]=='!':
        p[i%4]+=1
    elif s[i] in col:
        t=col.index(s[i])
        sootv[t]=i%4
print(' '.join([str(p[sootv[i]]) for i in range(4)]))
