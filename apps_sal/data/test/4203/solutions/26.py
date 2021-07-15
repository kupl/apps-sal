s = list(input())
flg = "WA"
if s[0]=="A":
  if "C" in s[2:len(s)-1]:
    s.remove("A")
    s.remove("C")
    s = ''.join(s)
    if s.islower()==True:
      flg = "AC"
print(flg)
