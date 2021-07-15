a,b = map(str,input().split())
from math import sqrt
print("Yes" if sqrt(int(a+b)) == int(sqrt(int(a+b))) else "No")
