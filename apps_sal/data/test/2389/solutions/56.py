n,a,b,c=map(int,input().split())
s=[input()for _ in range(n)]
if (a+b+c)==0:
  print("No")
if (a+b+c)==1 or (a+b+c)>=3:
  ans=[]
  for i in s:
    if i=="AB":
      if a<b:ans.append("A");a+=1;b+=-1;c+=0
      else:ans.append("B");a+=-1;b+=1;c+=0
    if i=="BC":
      if b<c:ans.append("B");a+=0;b+=1;c+=-1
      else:ans.append("C");a+=0;b+=-1;c+=1
    if i=="AC":
      if a<c:ans.append("A");a+=1;b+=0;c+=-1
      else:ans.append("C");a+=-1;b+=0;c+=1
    if min(a,b,c)<0:
      print("No");return
  print("Yes")
  for i in ans:print(i)
if (a+b+c)==2:
  ans=[]
  for i in range(n-1):
    if s[i]=="AB":
      if a==b:
        if s[i+1]=="AC":ans.append("A");a+=1;b+=-1;c+=0
        else:ans.append("B");a+=-1;b+=1;c+=0
      elif a<b:ans.append("A");a+=1;b+=-1;c+=0
      else:ans.append("B");a+=-1;b+=1;c+=0
    if s[i]=="BC":
      if b==c:
        if s[i+1]=="AC":ans.append("C");a+=0;b+=-1;c+=1
        else:ans.append("B");a+=0;b+=1;c+=-1
      elif b<c:ans.append("B");a+=0;b+=1;c+=-1
      else:ans.append("C");a+=0;b+=-1;c+=1
    if s[i]=="AC":
      if a==c:
        if s[i+1]=="BC":ans.append("C");a+=-1;b+=0;c+=1
        else:ans.append("A");a+=1;b+=0;c+=-1
      elif a<c:ans.append("A");a+=1;b+=0;c+=-1
      else:ans.append("C");a+=-1;b+=0;c+=1
    if min(a,b,c)<0:
      print("No");return
  for i in s[n-1:]:
    if i=="AB":
      if a<b:ans.append("A");a+=1;b+=-1;c+=0
      else:ans.append("B");a+=-1;b+=1;c+=0
    if i=="BC":
      if b<c:ans.append("B");a+=0;b+=1;c+=-1
      else:ans.append("C");a+=0;b+=-1;c+=1
    if i=="AC":
      if a<c:ans.append("A");a+=1;b+=0;c+=-1
      else:ans.append("C");a+=-1;b+=0;c+=1
    if min(a,b,c)<0:
      print("No");return
  print("Yes")
  for i in ans:print(i)
