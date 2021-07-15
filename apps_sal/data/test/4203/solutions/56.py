import re
S = input()
if S[0].isupper() and S[2:-1].count("C")==1 and re.sub(r"[AC]","",S).islower():
  print("AC")
else:
  print("WA")
