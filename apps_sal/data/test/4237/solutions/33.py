A,B,C,D = map(int,input().split())
import math
E = C*D//math.gcd(C,D)
A -= 1
c = B//C - A//C
d = B//D - A//D
e = B//E - A//E
print(B-A-(c+d-e))
