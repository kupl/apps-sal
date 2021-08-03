import numpy as np

a, b = input().split(' ')

c = int(a + b)

sqrt_c = np.sqrt(c) // 1

if(sqrt_c**2 == c):
    print("Yes")
else:
    print("No")
