import sys
input = sys.stdin.readline
n, a, b, c = map(int, input().split())
S = [input().rstrip().replace("AC", "CA") for _ in range(n)]
D = ["AB", "BC", "CA"]
X = [a+b, b+c, c+a]
L = []
for i, s in enumerate(S):
  k = D.index(s)
  if X[k] == 0:
    print("No")
    return
  if X[(k+1)%3] == 1 and X[(k+2)%3] == 1 and i < n-1:
    l = D.index(S[i+1])
    if l == (k+1)%3:
      X[(k+1)%3] += 1
      X[(k+2)%3] -= 1
      L.append(s[1])
    else:
      X[(k+2)%3] += 1
      X[(k+1)%3] -= 1
      L.append(s[0])
  else:
    if X[(k+1)%3] < X[(k+2)%3]:
      X[(k+1)%3] += 1
      X[(k+2)%3] -= 1
      L.append(s[1])
    else:
      X[(k+2)%3] += 1
      X[(k+1)%3] -= 1
      L.append(s[0])
print("Yes")
print(*L, sep="\n")
