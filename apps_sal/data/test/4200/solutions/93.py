N = list(map(int,input().split()))
A = list(map(int,input().split()))
sorted_A = sorted(A,reverse=True)
sum_A =sum(A)
flag = 0
for i in range(N[1]):
  if(sorted_A[i]>=sum_A/(4*N[1])):flag = 1
  else:flag = 0
if(flag == 1):print("Yes")
else:print("No")
