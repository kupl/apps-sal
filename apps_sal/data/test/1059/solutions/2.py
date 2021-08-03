import math
n = int(input().strip())
q = 0
for k in range(5, n + 1):
    if(n % k == 0 and (n // k) >= 5):
        a = k
        b = n // k
        q = 1
pp = ['a', 'e', 'i', 'o', 'u']
if(q == 0):
    print(-1)
else:
    start = 0
    ss = ""
    for t in range(a):
        for tt in range(b):
            ss = ss + pp[(t + tt) % 5]
    print(ss)
