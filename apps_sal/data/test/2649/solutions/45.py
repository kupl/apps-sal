N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
  x,y = map(int,input().split())
  A[i] = x+y
  B[i] = x-y
a = max(A)-min(A)
b = max(B)-min(B)
print(max(a,b))
