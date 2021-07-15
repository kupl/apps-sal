N, L = list(map(int, input().split()))
stk = []
ans = []
for i in range(N):
  tmp = L + i
  stk.append(tmp)

for i in range(N):
  tmp1 = sum(stk)
  tmp = stk[i]
  stk[i] = 0
  tmp2 = sum(stk)
  stk[i] = tmp
  ans.append(abs(tmp1 - tmp2))

tmp = min(ans)

if tmp in stk:
  stk.remove(tmp)
  print(sum(stk))
else:
  stk.remove(-tmp)
  print(sum(stk))
