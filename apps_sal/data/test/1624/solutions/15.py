n=int(input())
a=list(map(int,input().split()))
a.sort()
s=0
for i in range(n//2):
  s+=pow((a[i]+a[n-i-1]),2)
print(s)


