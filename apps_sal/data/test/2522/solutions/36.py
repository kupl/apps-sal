N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

T = [(A[i], i) for i in range(N)]+[(B[i], N+i) for i in range(N)]
T.sort()

P = [-1]*(2*N)
for i in range(N):
  if T[i][0]==T[i+N][0]:
    print("No")
    return
  P[T[i][1]] = T[i+N][1]
  P[T[i+N][1]] = T[i][1]

bp1 = N
for ap1 in range(N):
  if P[ap1]//N==1:
    continue
  while P[bp1]//N==0:
    bp1 += 1
  ap2 = P[ap1]
  bp2 = P[bp1]
  if A[ap1]!=B[bp1-N] and A[ap2]!=B[bp2-N]:
    P[ap1] = bp1
    P[bp1] = ap1
    P[ap2] = bp2
    P[bp2] = ap2
  else:
    P[ap1] = bp2
    P[bp1] = ap2
    P[ap2] = bp1
    P[bp2] = ap1

print("Yes")
print((" ".join(str(B[P[i]-N]) for i in range(N))))

