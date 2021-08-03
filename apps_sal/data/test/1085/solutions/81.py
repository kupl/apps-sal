import math
N = int(input())
a = 0
for i in range(1, int(math.sqrt(N - 1)) + 1):
    if (N - 1) % i == 0:
        a += 2
        i += 1
    else:
        i += 1
a -= 1

if int(math.sqrt(N - 1)) == math.sqrt(N - 1):
    a -= 1
for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        t = N
        while t % i == 0:
            t = t / i
        if t % i == 1:
            a += 1
            i += 1
        else:
            i += 1
a += 1
print(a)
