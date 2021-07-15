N = int(input())
A = list(map(int,input().split()))
S1 = A[0]
S2 = sum(A)-A[0]
B = [abs(S1-S2)]

for i in range(N-2):
  S1 += A[i+1]
  S2 -= A[i+1]
  B.append(abs(S1-S2))

print(min(B))
