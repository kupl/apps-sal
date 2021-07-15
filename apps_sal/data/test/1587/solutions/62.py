N=int(input())
S=input()
i=0
j=N-1
ans=0
while True:
    while S[j]=='W':
        j-=1
        if j<0:
            break
    while S[i]=='R':
        i+=1
        if i>=N:
            break
    if j<i:
        break
    ans+=1
    i+=1
    j-=1
    if j<i:
        break
print(ans)

