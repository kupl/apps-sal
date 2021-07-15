import sys
readline = sys.stdin.readline

X,Y,Z,K = map(int,readline().split())

A = sorted(list(map(int,readline().split())),reverse = True)
B = sorted(list(map(int,readline().split())),reverse = True)
C = sorted(list(map(int,readline().split())),reverse = True)

ans = []
for a in range(len(A)):
  for b in range(len(B)):
    for c in range(len(C)):
      if (a + 1) * (b + 1) * (c + 1) > K:
        break
      ans += [A[a] + B[b] + C[c]]
      
ans = sorted(ans,reverse = True)[:K]
print(*ans,sep = "\n")
