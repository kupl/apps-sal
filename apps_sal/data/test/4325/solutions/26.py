inp=input()
n=int(inp.split()[0])
x=int(inp.split()[1])
t=int(inp.split()[2])
import math
if n%x!=0:
  value=int(n/x)+1
else:
  value=n/x
print(int(value*t))
