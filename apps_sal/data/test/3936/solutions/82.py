n = int(input())
s1=input()
s2=input()
k=1
i=0
if s1[0]==s2[0]:
    i+=1
    k=3
else:
    i+=2
    k=6
mod=1000000007
while i<n:
    if s1[i]!=s2[i] and s1[i-1]!=s2[i-1]:
        k*=3
        i+=2
    elif s1[i]!=s2[i] and s1[i-1]==s2[i-1]:
        k*=2
        i+=2
    else:
        if s1[i-1]==s2[i-1]:
            k*=2
        i+=1
    k%=mod
print(k)
        

