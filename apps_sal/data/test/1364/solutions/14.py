n=int(input(''))
s=list(map(int,input('').split()))
ans=0
for i in range(len(s)-1):
    if s[i]*s[i+1]==2:
        j=1
        while (i-j)>=0 and (i+1+j)<n:
            if s[i-j]==s[i-j+1] and s[i+1+j]==s[i+j]:
                j+=1
            else:
                break
        ans=max(ans,j)
print(ans*2)

