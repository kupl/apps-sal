from collections import defaultdict

s = input()
t = input()

AL = "abcdefghijklmnopqrstuvwxyz"
S = defaultdict(int)
T = defaultdict(int)

for al in s:
  S[al] += 1

for al in t:
  T[al] += 1

ans_s = ""
for al in AL:
  ans_s += al*S[al]

ans_t = ""
for al in reversed(list(AL)):
  ans_t += al*T[al]

if ans_s < ans_t:
  print("Yes")
else:
  print("No")
