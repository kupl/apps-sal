N=int(input())
a=list()
for _ in range(N):
  A,B=list(map(int,input().split()))
  a.append((B,A))
a.sort()
t=0
for i in range(N):
  t+=a[i][1]
  if t>a[i][0]:
    print("No")
    return
print("Yes")

