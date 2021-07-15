n,m = map(int,input().split())
l= list(map(int,input().split()))
l_sorted = sorted(l,reverse=True)
border = sum(l)/(4*m)
temp = []
for i in range(m):
  if(border <= l_sorted[i]):
    temp.append(1)
 
print('Yes' if sum(temp)==m else 'No')
