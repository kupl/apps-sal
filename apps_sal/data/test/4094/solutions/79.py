from time import time

K = int(input())
t = time()

i = 1
n = 7%K
m = 10%K
while time()-t < 1.95:
    if n == 0:
        print(i)
        break
    n += 7*m
    n %= K
    m = m*10%K
    i += 1
else:
    print(-1)
