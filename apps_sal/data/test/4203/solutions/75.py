S = input()
check = False
if S[0] == "A" and "C" in S[2:-1]:
  i = list(S).index("C")
  T = S[1:i] + S[i+1:]
  if T == T.lower():
    check = True
    
print("AC" if check else "WA")  
