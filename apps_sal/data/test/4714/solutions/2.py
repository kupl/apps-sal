A, B = [int(x) for x in input().split()]
ans = 0
for i in range(A, B+1):
  s = str(i)
  S = list(s)
  if(S[0]==S[4] and S[1]==S[3]):
    ans += 1
print(ans)
