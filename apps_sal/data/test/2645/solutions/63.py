s = list(input())
T_g = s.count("g")
T_p = s.count("p")

if T_g == T_p or T_g == T_p+1:
  result = 0
  print(result)
  return
else:
  P = (T_g + T_p) // 2
  result = P - T_p
  print(result)

