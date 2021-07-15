import math

t = int(input())


for qq in range(t):
    n = int(input())
    step = 2
    s = 0
    val = 1
    while n >= step // 2:
        k = n - (step // 2)
        s += val
        s += val * (k // step)
        step *= 2
        val += 1
        #print(s, end = ' ')
    print(s)

