n=int(input())
arr=list(map(int,input().strip().split(' ')))
d={}
i = 0
while(i<n):
  try:
    t = d[arr[i]]
    arr[t] = -1
    del d[arr[i]]
    arr[i] = 2*arr[i]
  except KeyError:
    d[arr[i]] = i
    i+=1
print(n-arr.count(-1))
for i in range(n):
  if(arr[i]!=-1):
    print(arr[i],end=' ')


