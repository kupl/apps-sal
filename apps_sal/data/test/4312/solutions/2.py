a,b,c,d = map(int, input().split())
import math
print('Yes' if math.ceil(c/b) <= math.ceil(a/d) else 'No')
