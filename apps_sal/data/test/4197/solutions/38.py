n = int(input())
A = list(map(int,input().split()))
L = [0]*n
for i in range(n):
  L[A[i]-1] = i + 1
print(*L)
