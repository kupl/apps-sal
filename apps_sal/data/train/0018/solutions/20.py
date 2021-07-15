import random
import math
LI = lambda: list(map(int,input().split()))
MI = lambda: map(int,input().split())
yes = lambda: print("Yes")
no = lambda: print("No")
I = lambda: list(input())
J = lambda x: "".join(x)
II = lambda: int(input())
SI = lambda: input()
#---khan17---template
t = II()
for q in range(t):
	n = II()
	R = 1/(2*math.sin(math.pi/(2*n)))
	r = math.sqrt(R**2-0.25)
	print(2*r)
