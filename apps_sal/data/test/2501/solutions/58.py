N = int(input())
A = list(map(int, input().split()))
ans = 0
B = []
C = []
maA = max(A) + N -1
for k in range(N):
  if A[k] + k <= maA:
    B.append(A[k]+k)
  if -A[k] + k >0:
    C.append(-A[k]+k)
B.sort()
C.sort()

c = 0
b = 0
while b < len(B) and c < len(C):
  if B[b] == C[c]:
    s = 0
    t = 0
    j = float('inf')
    k = float('inf')
    for j in range(b, len(B)):
      if B[b] == B[j]:
        s += 1
      else:
        break
    for k in range(c, len(C)):
      if C[c] == C[k]:
        t +=1
      else:
        break
    ans += s*t
    b = j
    c = k
    continue
  elif B[b] > C[c]:
    c += 1
  else:
    b += 1
#print(B)
#print(C)
print(ans)
