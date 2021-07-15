A,B=map(int,input().split())
import math
a=math.gcd(A,B)
ans=A*B//a
print(ans)
