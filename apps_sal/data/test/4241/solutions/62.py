import sys
readline = sys.stdin.readline

S = readline().rstrip()
T = readline().rstrip()

ans = 10 ** 10
for s_ind in range(len(S)):
  if s_ind + len(T) > len(S):
    break
  change = 0
  for t_ind in range(len(T)):
    if T[t_ind] != S[s_ind + t_ind]:
      change += 1
      if change > ans:
        break
  if ans > change:
    ans = change

print(ans)
