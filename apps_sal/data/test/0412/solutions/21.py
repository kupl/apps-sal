import math

n = int(input())
a = [int(i) for i in input().split()]


def checkStepen(a):
    stepen = 0
    while True:
        if a % 2 == 0:
            a //= 2
            stepen += 1
        else:
            break
    return 2**stepen


r = 0
max = 0
for i in a:
    k = checkStepen(i)
    if(k > r):
        max = 1
        r = k
    elif (k == r):
        max += 1
print(r, max)
