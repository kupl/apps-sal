n,a,b,c=map(int,input().split())
s=list(input() for i in range(n))+["XX"]
ans=["Yes"]

if a+b+c==0:
  del ans[:]
  ans+=["No"]
  
if a+b+c==1:
  for j in range(n):
    
    if s[j]=="AB":
      if c==1:
        del ans[:]
        ans+=["No"]
        break        
      elif a==1:
        a-=1
        b+=1
        ans+=["B"]
      elif b==1:
        a+=1
        b-=1
        ans+=["A"]

    if s[j]=="AC":
      if b==1:
        del ans[:]
        ans+=["No"]
        break       
      elif a==1:
        a-=1
        c+=1
        ans+=["C"]
      elif c==1:
        a+=1
        c-=1
        ans+=["A"] 

    if s[j]=="BC":
      if a==1:
        del ans[:]
        ans+=["No"]
        break
      elif b==1:
        b-=1
        c+=1
        ans+="C"
      elif c==1:
        b+=1
        c-=1
        ans+=["B"]  

if a+b+c==2:
  for j in range(n):
    if s[j]=="AB":
      if a==2:
        a-=1
        b+=1
        ans+=["B"]
      elif b==2:
        a+=1
        b-=1
        ans+=["A"]
      elif c==2:
        del ans[:]
        ans+=["No"]
        break     
      elif (a==1 and b==1) and (s[j+1]=="AB" or s[j+1]=="AC" or s[j+1]=="XX"):
        a+=1
        b-=1
        ans+=["A"]
      elif (a==1 and b==1) and (s[j+1]=="BC"):
        a-=1
        b+=1
        ans+=["B"]
      elif a==1 and c==1:
        a-=1
        b+=1
        ans+=["B"]
      elif b==1 and c==1:
        a+=1
        b-=1
        ans+=["A"]
    
    if s[j]=="AC":
      if a==2:
        a-=1
        c+=1
        ans+=["C"]
      elif c==2:
        a+=1
        c-=1
        ans+=["A"] 
      elif b==2:
        del ans[:]
        ans+=["No"]
        break     
      elif (a==1 and c==1) and (s[j+1]=="AB" or s[j+1]=="AC" or s[j+1]=="XX"):
        a+=1
        c-=1
        ans+=["A"]
      elif (a==1 and c==1) and (s[j+1]=="BC"):
        a-=1
        c+=1
        ans+=["C"]
      elif a==1 and b==1:
        a-=1
        c+=1
        ans+=["C"]
      elif b==1 and c==1:
        a+=1
        c-=1
        ans+=["A"]

    if s[j]=="BC":
      if c==2:
        c-=1
        b+=1
        ans+=["B"]
      elif b==2:
        c+=1
        b-=1
        ans+=["C"] 
      elif a==2:
        del ans[:]
        ans+=["No"]
        break     
      elif (c==1 and b==1) and (s[j+1]=="AB" or s[j+1]=="BC" or s[j+1]=="XX"):
        b+=1
        c-=1
        ans+=["B"]
      elif (c==1 and b==1) and (s[j+1]=="AC"):
        b-=1
        c+=1
        ans+=["C"]
      elif a==1 and c==1:
        c-=1
        b+=1
        ans+=["B"]
      elif b==1 and a==1:
        c+=1
        b-=1
        ans+=["C"]        

if a+b+c>=3:
  if s[0]=="AB" and a+b==0 or s[0]=="AC" and a+c==0 or s[0]=="BC" and b+c==0:
    del ans[:]
    ans+=["No"]
  
  else:
    for j in range(n):
      if s[j]=="AB":
        if a>b:
          a-=1
          b+=1
          ans+=["B"]
        elif a<=b:
          a+=1
          b-=1
          ans+=["A"]
        
      if s[j]=="AC":
        if a>c:
          a-=1
          c+=1
          ans+=["C"]
        elif a<=c:
          a+=1
          c-=1
          ans+=["A"]     

      if s[j]=="BC":
        if b>c:
          b-=1
          c+=1
          ans+=["C"]
        elif b<=c:
          b+=1
          c-=1
          ans+=["B"]

for an in ans:
  print(an)
