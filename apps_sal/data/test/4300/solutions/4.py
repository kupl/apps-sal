n = int(input())
xlist = list(map(int,input().split()))
sum = 0
for i in range(n):
  for j in range(i+1,n):
    sum+=xlist[i]*xlist[j]
print(sum)
