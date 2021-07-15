N = int(input())
S = list(input())
R = []
G = []
for i in range(N):
  if S[i] == "R":
    R.append(i)
  elif S[i] == "G":
    G.append(i)
r = len(R)
g = len(G)
ans = r * g * (N - r - g)
for i in R:
  for j in G:
    a = 2 * i - j
    b = 2 * j - i
    c = i + j
    if 0 <= a < N and S[a] == "B":
      ans -= 1
    if 0 <= b < N and S[b] == "B":
      ans -= 1
    if c % 2 == 0 and S[c//2] == "B":
      ans -= 1
print(ans)
