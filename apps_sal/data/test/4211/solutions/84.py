N = int(input())
B = list(map(int,input().split()))

B = B[::-1]
A = []
for i in range(N):
  if i == 0:
    A.append(B[0])
  elif i >= N - 1:
    A.append(B[i-1])
  else:
    a = min(B[i],B[i-1])
    A.append(a)
    
print(sum(A))
