s = str(input())
if int(s[0:4]) < 2019:
  print("Heisei")
elif int(s[0:4]) < 2020 and int(s[5:7]) <= 4:
  print("Heisei")
else:
  print("TBD")
