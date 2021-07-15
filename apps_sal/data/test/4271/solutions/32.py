N = int(input())
A = list((int(x) for x in input().split()))
B = list((int(x) for x in input().split()))
C = list((int(x) for x in input().split()))
bonus = 0
for i in range(N-1):
  if A[i]+1 == A[i+1]:
    bonus += C[A[i]-1]
print(sum(B)+bonus)
