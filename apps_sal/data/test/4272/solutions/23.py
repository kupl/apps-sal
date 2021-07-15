_=input()
S=input()
cnt = 0
for a,b,c in zip(S[0:],S[1:],S[2:]):
  if "ABC" == a+b+c:
    cnt += 1
print(cnt)
