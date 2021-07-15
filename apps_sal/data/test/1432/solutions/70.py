N = int(input())
A = list(map(int,input().split()))
B = [2*sum(A[::2])-sum(A)]

for n in range(N-1):
  B+=[2*A[n]-B[n]]

print(*B)
