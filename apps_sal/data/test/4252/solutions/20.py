n=int(input())
ch=input()
ans=0
c=0
for i in range(n):
      if ch[i]=="x":
            c+=1
      if (ch[i]=="x" and i==n-1) or ch[i]!="x":
            if c>=3:
                  ans+=(c-2)
            c=0
print(ans)
      

