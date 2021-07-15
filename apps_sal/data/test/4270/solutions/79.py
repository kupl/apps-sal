M = int(input())
A = list(map(int,input().split()))
A.sort()
count = 0
count = (A[0]+A[1])/2
for i in range(2,M):
  count = (count+A[i])/2
  
print(count)
