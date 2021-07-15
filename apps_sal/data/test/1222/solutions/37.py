K = int(input())
A = [1,2,3,4,5,6,7,8,9]

for i in A:
  if K<len(A):
    break
  x = i%10
  for j in range(max(x-1,0),min(x+2,10)):
    A.append(10*i+j)

print(A[K-1])
