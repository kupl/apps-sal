import math

def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


tt = int(input())

print(binom(tt,tt//2)*math.factorial(tt//2-1)*math.factorial(tt//2-1)//2)
