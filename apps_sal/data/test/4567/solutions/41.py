N = int(input())
S = []

for i in range(N):
  S.append(int(input()))
  
S.sort()
ans = sum(S)

if ans % 10 != 0:
  print(ans)
  return
  
for i in range(N):
  if S[i] % 10 != 0:
    ans -= S[i]
    print(ans)
    return

print((0))

