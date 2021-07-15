li=[]
ans=0
for i in range(4):
  li.append(int(input()))
if li[0]<li[1]:
  ans+=li[0]
else:
  ans+=li[1]
if li[2]<li[3]:
  ans+=li[2]
else:
  ans+=li[3]
print(ans)
