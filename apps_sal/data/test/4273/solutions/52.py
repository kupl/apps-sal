from itertools import combinations
N = int(input())

march = [0] * 5
for _ in range(N):
  S = input()
  S = S[0]
  if S == "M":
    march[0] += 1
  elif S == "A":
    march[1] += 1
  elif S == "R":
    march[2] += 1
  elif S == "C":
    march[3] += 1
  elif S == "H":
    march[4] += 1
  
ls = list(combinations(range(5),3))

ans = 0
for (i,j,k) in ls:
  ans += march[i] * march[j] * march[k]
  
print(ans)
