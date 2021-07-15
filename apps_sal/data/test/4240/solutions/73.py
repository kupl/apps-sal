
s=input()
t=input()
n=0

for i in range(len(s)):
    a=len(s)-1


    s=s[a]+s[0:a]
  
    if s==t:
        n=1
        break
        
        
if n==1:
    if len(s)==len(t):
        print("Yes")
else:
    print("No")
