O = input()
E = input()
S = ""

if len(O) == len(E):
  for i in range(len(O)):
    S += O[i] + E[i]
    
else:
  for i in range(len(E)):
    S += O[i] + E[i]
  S += O[len(O)-1]
  
print(S)
