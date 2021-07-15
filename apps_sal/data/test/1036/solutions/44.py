import sys
readline = sys.stdin.readline

N,K = map(int,readline().split())
S = readline().rstrip()

S *= 2
N *= 2

WIN = {"RP":"P","PR":"P","PS":"S","SP":"S","SR":"R","RS":"R"}
def win(a,b):
  if a == b:
    return a
  return WIN[a + b]
  

for k in range(K):
  newS = ""
  for i in range(N // 2):
    newS += win(S[i * 2],S[i * 2 + 1])
  S = newS * 2

print(S[0])
