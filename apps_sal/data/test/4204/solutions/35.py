S = str(input())
N = int(input())
Ones = 0
nxt = ""
for i in range(len(S)):
  if S[i] == "1":
    Ones += 1
  else:
    nxt = S[i]
    break
if N <= Ones:
  print((1))
else:
  print(nxt)

