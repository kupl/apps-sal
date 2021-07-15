N = int(input())
A = list(map(int, input().split()))

tmp = 0
for i in range(N//2):
  tmp += A[2*i+1]
  
ans = []
if sum(A) > 2*tmp:
  ans.append(sum(A)-2*tmp)
else:
  ans.append(0)
  
for i in range(N-1):
  ans.append(2*A[i]-ans[-1])
print((*ans))

