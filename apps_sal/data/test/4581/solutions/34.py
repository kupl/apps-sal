str = input()
cnt = 700
if str[0]=="o" and str[1]=="o" and str[2]=="o":
  cnt = 1000
elif (str[0]=="o" and str[1]=="o") or (str[1]=="o" and str[2]=="o") or(str[0]=="o" and str[2]=="o"):
  cnt = 900
elif str[0]=="o" or str[1]=="o" or str[2]=="o":
  cnt = 800
print(cnt)
