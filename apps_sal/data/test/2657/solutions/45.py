n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
cand=a[1]
for i in range(1,n-1):
  if abs(a[0]/2 - a[i]) > abs(a[0]/2 - a[i+1]):
    cand = a[i+1]
  else:
    break
print(a[0], cand)
