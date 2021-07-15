n=int(input())
s=[]
for i in range(n):
    tmp=input().split()
    tmp[1]=100-int(tmp[1])
    s.append(tmp+[str(i+1)])
s=sorted(s)

for i in range(n):
    print((s[i][-1]))

