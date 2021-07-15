s = [int(x) for x in input().split("/")]
 
if s[1] < 4:
  print("Heisei")
elif s[1] == 4 and s[2] <= 30:
  print("Heisei")
else:
  print("TBD")
