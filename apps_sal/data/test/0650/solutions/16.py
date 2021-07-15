NEAT="AEFHIKLMNTVWXYZ"
a=input()

if all(x in NEAT for x in a) or all(x not in NEAT for x in a) :
               print("YES")
else:
               print("NO")
