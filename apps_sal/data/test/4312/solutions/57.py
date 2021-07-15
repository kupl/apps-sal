A,B,C,D = list(map(int,input().split()))
import math
print(("Yes" if math.ceil(C/B) <= math.ceil(A/D) else "No"))

