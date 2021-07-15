import math

n = int(input())

def S(n):
    return sum(map(int,list(str(n))))

base = 10**int(math.log10(n))
a = base-1
res = 0
for i in range(10):
    b = n-a
    res = max(res, S(a)+S(b))
    a+=base
    if a > n:
        break
print(res)

