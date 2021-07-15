import numpy as np

n = int(input())
a = list(map(int,input().split()))

gcd = np.frompyfunc(np.gcd,2,1)

print(gcd.reduce(a))
