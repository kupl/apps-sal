s = input()
if len(s)<4:
  print("WA")
else:
  if s[0]!="A":
    print("WA")
  else:
    if s[2:-1].count("C")!=1:
      print("WA")
    else:
      tmp = s[1]+s[2:].replace("C","c")
      if tmp != tmp.lower():
        print("WA")
      else:
        print("AC")
