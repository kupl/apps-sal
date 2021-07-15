s1 = input()
s1 = s1.split()
n = int(s1[0])
d = int(s1[1])
s = input()
count = 0
pos = 1
dk = d
res = True
while(pos!=n):
    if dk==0:
        res = False
        break
    if pos+dk<=n and s[pos+dk-1]=='1':
        if dk==0:
            res = False
            break
        pos+=dk
        count+=1
        dk = d
    else:
        dk-=1

if res:
    print(count)
else:
    print(-1)
