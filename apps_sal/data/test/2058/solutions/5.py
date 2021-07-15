import math
import itertools

a = [int(x) for x in input().rstrip()]
b = [int(x) for x in input().rstrip()]
n = len(a)
m = len(b)
prefix_b = [0] + list(itertools.accumulate(b))
res = 0
for i in range(n):
    ones = prefix_b[-n+i] - prefix_b[i]
    res += m-n+1 - ones if a[i] else ones
print(res)
    

    

