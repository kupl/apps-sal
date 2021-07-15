n=int(input())
a=list(map(int,input().split()))

a.sort()

maxa=max(a)
ans=0
ch=0

for i in range(n-1):
  b=maxa-a[i]
  c=min(b,a[i])
  if c>=ch:
    ans=a[i]
    ch=c
    
print(str(maxa)+' '+str(ans))
