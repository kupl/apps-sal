l=list(map(int,input().split()))
ans=t=sum(l)
for i in range(5):
  for j in range(i+1,5):
    if l[i]==l[j] and t-l[i]-l[j]<ans: ans=t-l[i]-l[j]
for i in range(5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      if l[i]==l[j]==l[k] and t-l[i]-l[j]-l[k]<ans: ans=t-l[i]-l[j]-l[k]
print(ans)

