n=int(input().strip())
ss=input().strip()
q=0
for k in range(n):
    if(ss[k]=="("):
        q+=1
ii=(n//2)-q
count=0
s=""
if(n%2!=0):
    print(":(")
elif(ii<0):
    print(":(")
else:
 for k in range(n):
    if(ss[k]=="?" and count<ii):
        s=s+"("
        count+=1
    elif(ss[k]=="?" and count>=ii):
        s=s+")"
    elif(ss[k]=="("):
        s=s+"("
    else:
        s=s+")"
 c2=0
 c3=0
 for  k in range(n-1):
     if s[k]=="(":
       c2+=1
     else:
       c3+=1
     if(c3>=c2):
         print(":(")
         break
 else:
     if s[n-1]=="(":
       c2+=1
     else:
       c3+=1
     if(c2!=c3):
         print(":(")
     else:
         print(s)
