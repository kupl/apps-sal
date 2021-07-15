N,M = map(int,input().split())
A = list(map(int,input().split()))
BC = [list(map(int,input().split())) for m in range(M)]
BC = sorted(BC,key=lambda x:x[1])[::-1]

for b,c in BC:
  A.extend(b*[c])
  if 2*N<len(A):
    break

A = sorted(A)[::-1]
print(sum(A[:N]))
