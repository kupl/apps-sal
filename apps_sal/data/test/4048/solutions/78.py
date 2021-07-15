import math
N = int(input())
M = []
sqr_N = math.floor(math.sqrt(N))
a = 0
    
for i in range(1, (sqr_N + 1)):
    if N % i == 0:
        a = i

a_pair = N // a
print(a + a_pair - 2)
