N=int(input())
L=list(map(int,input().split()))
L.sort()
sum=0
for i in range(0,2*N,2):
  sum+=L[i]
print(sum)
