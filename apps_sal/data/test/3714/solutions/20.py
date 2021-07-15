#from collections import deque
from functools import reduce

n = int(input())
crush = [int(i) - 1 for i in input().split()]

def parity_treat(n):
    if n%2 == 0:
        return n//2
    else:
        return n

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

def lcmm(*args):
    return reduce(lcm, args)


if len(set(crush)) < n:
    print(-1)
else:
    component_size = []
    visited = set()
    for i in range(n):
        if i not in visited:
            tmp = 1
            start = i
            visited.add(start)
            j = crush[start]
            while j !=  start:
                visited.add(j)
                j = crush[j]
                tmp+=1
            component_size.append(tmp)
    component_size = [parity_treat(i) for i in component_size]
    print(lcmm(*component_size))
