N = int(input())
S = []
ans = 0

for i in range(N):
  s = list(input())
  s.sort()
  S.append("".join(s))

S.sort()

count = 1

for j in range(N-1):
  if S[j] == S[j+1]:
    count += 1
  else:
    if count > 1:
      ans += count*(count-1)//2
    count = 1
else:
    if count > 1:
      ans += count*(count-1)//2

print(ans)
