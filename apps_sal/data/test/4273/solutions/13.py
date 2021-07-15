n=int(input())
l=[0,0,0,0,0]
for _ in range(n):
    s=input()
    if s[0]=='M':l[0]+=1
    if s[0] == 'A': l[1] += 1
    if s[0] == 'R': l[2] += 1
    if s[0] == 'C': l[3] += 1
    if s[0] == 'H': l[4] += 1

for i in l:
    if i==0:l.remove(i)
total=len(l)
if total<3:ans=0
else:
    ans=0
    for i in range(0,total-2):
        for j in range(i+1,total-1):
            for k in range(j+1,total):
                ans+=l[i]*l[j]*l[k]
print(ans)
