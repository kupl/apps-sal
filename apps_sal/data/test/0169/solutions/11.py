import collections
import math

def is_prime(x): 
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

n = int(input())
a = int(input())
b = int(input())
c = int(input())
ans = 0
if b - c < a:
    if b < n:
        ans += (n - b) // (b - c)
        n = b + (n - b) % (b - c)
    while n >= b:
        ans += n // b
        n = n % b + n // b * c
ans += n // a
print(ans)
