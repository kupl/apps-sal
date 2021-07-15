n=int(input())
l=[0,0,0,0,0]
for _ in range(n):
    s=input()
    if s[0]=='M':l[0]+=1
    if s[0] == 'A': l[1] += 1
    if s[0] == 'R': l[2] += 1
    if s[0] == 'C': l[3] += 1
    if s[0] == 'H': l[4] += 1

ans=0
for i in range(0,5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            ans+=l[i]*l[j]*l[k]
print(ans)
