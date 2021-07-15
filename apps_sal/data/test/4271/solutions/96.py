n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
satisfy=0
for i in range(n):
  satisfy+=b[a[i]-1]
  if i>=1 and a[i-1]+1==a[i]:
    satisfy+=c[a[i]-2]
print(satisfy)
