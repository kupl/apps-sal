n,a,b,c=map(int,input().split())
arr=[input() for _ in range(n)]
ans=[]
for i in range(n):
  if arr[i]=='AB':
    if a==1 and b==1:
      if i==n-1 or arr[i+1]=='AB' or arr[i+1]=='AC':
        a+=1
        b-=1
        ans.append('A')
      elif arr[i+1]=='BC':
        a-=1
        b+=1
        ans.append('B')
    elif a==0 and b==0:
      print('No')
      break
    else:
      if a>=b:
        a-=1
        b+=1
        ans.append('B')
      else:
        a+=1
        b-=1
        ans.append('A')
  elif arr[i]=='AC':
    if a==1 and c==1:
      if i==n-1 or arr[i+1]=='AC' or arr[i+1]=='AB':
        a+=1
        c-=1
        ans.append('A')
      elif arr[i+1]=='BC':
        a-=1
        c+=1
        ans.append('C')
    elif a==0 and c==0:
      print('No')
      break
    else:
      if a>=c:
        a-=1
        c+=1
        ans.append('C')
      else:
        a+=1
        c-=1
        ans.append('A')
  elif arr[i]=='BC':
    if b==1 and c==1:
      if i==n-1 or arr[i+1]=='BC' or arr[i+1]=='AB':
        b+=1
        c-=1
        ans.append('B')
      elif arr[i+1]=='AC':
        b-=1
        c+=1
        ans.append('C')
    elif b==0 and c==0:
      print('No')
      break
    else:
      if b>=c:
        b-=1
        c+=1
        ans.append('C')
      else:
        b+=1
        c-=1
        ans.append('B')
else:
  print('Yes')
  for i in range(n):
    print(ans[i])
