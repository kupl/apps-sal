n,a=map(int,input().split())
nums=[int(i)-a for i in input().split()]
d={0:1}
for i in nums:
  s = [[j, d[j]] for j in d]
  for j in s:
    if j[0] + i in d:
      d[j[0]+i] += j[1]
    else:
      d[j[0]+i] = j[1]
print(d[0]-1)
