n = int(input())
l = list(map(int,input().split()))
count = 0
maxcount = 0
for i in range(n-1):
  if l[i]>=l[i+1]:
    count+=1
    maxcount = max(maxcount,count)
  else:
    count = 0
print(maxcount)
