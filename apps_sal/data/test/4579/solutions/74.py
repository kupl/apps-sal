N = int(input())
S = []
for i in range(N):
  s = str(input())
  S.append(s)
T = set(S)
print(len(T))
