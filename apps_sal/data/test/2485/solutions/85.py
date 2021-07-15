import sys

H, W, M = map(int, input().split())
R = [0] * H
C = [0] * W
S = set()

for _ in range(M):
  h, w = map(int, input().split())
  S.add((h - 1, w - 1))
  R[h - 1] += 1
  C[w - 1] += 1

r = max(R)
c = max(C)

HL = [i for i in range(H) if R[i] == r]
WL = [j for j in range(W) if C[j] == c]
 
#print(r, HL)
#print(c, WL)
  
for h in HL:
  for w in WL:
    if not (h, w) in S:
      print(r + c)
      return

print(r + c - 1)
