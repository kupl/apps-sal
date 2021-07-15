S = input()
N = len(S)

if N == 2 and S[0] == S[1]:
  print(1, 2)
  return

for i in range(N-2):
  if len(set(S[i:i+3])) <= 2:
    print(i+1, i+3)
    return

print(-1, -1)
