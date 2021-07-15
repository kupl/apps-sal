N = int(input())
A = list(map(int,input().split()))
step = 0
sum = 0
for i in range(N-1):
  step = A[i]-A[i+1]
  if(step >= 1):
    sum = sum + step
    A[i+1] = A[i]
  else:continue
print(sum)
