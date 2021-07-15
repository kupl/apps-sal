n=int(input())
s=input()

lc=0
rc=0
l=0
r=0
ch=1

for i in range(len(s)):
    if(s[i]==')'):
        l+=1
        lc+=1
    else:
        r+=1
        rc+=1
        
    if(l-r>=2):
        ch=0
        
if(ch==1 and lc==rc):
    print("Yes")
else:
    print("No")
    

