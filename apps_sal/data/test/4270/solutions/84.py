a=int(input())
b=list(map(int,input().split()))
b.sort()
c=b[0]
for i in range (a-1):
  c=(c+b[i+1])/2
print(c)
