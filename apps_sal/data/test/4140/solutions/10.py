S = input()
ans = 0

if S[0]=="0":
  ans += S[0::2].count("1")
  ans += S[1::2].count("0")
  
else:
  ans += S[0::2].count("0")
  ans += S[1::2].count("1")
  
print(ans)
