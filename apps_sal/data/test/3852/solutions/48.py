n=int(input())
arr=list(map(int,input().split()))
arr=[[arr[i],i+1] for i in range(n)]
mins=[10**18,0]
maxs=[-10**18,0]
flag=True
for i in range(n):
  if arr[i][0]<mins[0]:
    mins=[arr[i][0],arr[i][1]]
  if arr[i][0]>maxs[0]:
    maxs=[arr[i][0],arr[i][1]]
cnt=0
ans=[]
if maxs[0]<0:
  for i in range(n):
    flag=False
elif mins[0]>=0:
  pass
else:
  if abs(mins[0])>maxs[0]:
    flag=False
    for i in range(n):
      if arr[i][0]>0:
        arr[i][0]+=mins[0]
        cnt+=1
        ans.append([mins[1],arr[i][1]])
  else:
    for i in range(n):
      if arr[i][0]<0:
        arr[i][0]+=maxs[0]
        cnt+=1
        ans.append([maxs[1],arr[i][1]])
rows=[]
tmp=[[arr[0][0],arr[0][1]]]
for i in range(1,n):
  if arr[i-1][0]<=arr[i][0]:
    tmp.append([arr[i][0],arr[i][1]])
  else:
    rows.append(tmp)
    tmp=[[arr[i][0],arr[i][1]]]
if len(tmp)!=0:
  rows.append(tmp)
if flag==True:
  for i in range(len(rows)-1):
    if len(rows[i])==1:
      if len(rows[i+1])==1:
        rows[i+1][0][0]+=rows[i][0][0]
        ans.append([rows[i][0][1],rows[i+1][0][1]])
  for i in range(len(rows)-1):
    if len(rows[i])==1:
      if len(rows[i+1])==1:
        continue
      else:
        for j in range(len(rows[i+1])):
          rows[i+1][j][0]+=rows[i][0][0]
          ans.append([rows[i][0][1],rows[i+1][j][1]])
    else:
      if len(rows[i+1])==1:
        for j in range(i+1,len(rows)):
          if len(rows[j])==1:
            rows[j][0][0]+=rows[i][-1][0]
            ans.append([rows[i][-1][1],rows[j][0][1]])
          else:
            break
      else:
        for j in range(len(rows[i+1])):
          rows[i+1][j][0]+=rows[i][-1][0]
          ans.append([rows[i][-1][1],rows[i+1][j][1]])
else:
  for i in range(len(rows)-1,0,-1):
    if len(rows[i])==1:
      if len(rows[i-1])==1:
        rows[i-1][0][0]+=rows[i][0][0]
        ans.append([rows[i][0][1],rows[i-1][0][1]])
  for i in range(len(rows)-1,0,-1):
    if len(rows[i])==1:
      if len(rows[i-1])==1:
        continue
      else:
        for j in range(len(rows[i-1])):
          rows[i-1][j][0]+=rows[i][0][0]
          ans.append([rows[i][0][1],rows[i-1][j][1]])
    else:
      if len(rows[i-1])==1:
        for j in range(i-1,-1,-1):
          if len(rows[j])==1:
            rows[j][0][0]+=rows[i][0][0]
            ans.append([rows[i][0][1],rows[j][0][1]])
          else:
            break
      else:
        for j in range(len(rows[i-1])):
          rows[i-1][j][0]+=rows[i][0][0]
          ans.append([rows[i][0][1],rows[i-1][j][1]])
print(len(ans))
for i in range(len(ans)):
  print(*ans[i])
