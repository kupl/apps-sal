from itertools import permutations
from math import factorial
n = int(input())
p = tuple(map(int, input().split(' ')))
q = tuple(map(int, input().split(' ')))

l = [i for i in range(1, n+1)]
ls = list(permutations(l))

for i in range(factorial(n)):
    if p==ls[i]:
        a = i
    if q==ls[i]:
        b = i

print(abs(a-b))
