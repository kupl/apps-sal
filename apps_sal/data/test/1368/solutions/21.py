import sys
from collections import Counter

def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact

N, A, B = map(int,input().split())
V = list(map(int,input().split()))

c1 = Counter(V)

V.sort(reverse = True)

if all([V[0] == i for i in V[:A]]):
    print(V[0])
    ans = 0
    for i in range(A-1, B):
        if V[i] != V[0]:
            break
        ans += factorial(c1[V[0]])//(factorial(c1[V[0]]-(i+1))*factorial(i+1))
    print(ans)
    return

print(sum(V[:A]) / A)

c2 = Counter(V[:A])

print(factorial(c1[V[A-1]])//(factorial(c1[V[A-1]]-c2[V[A-1]])*factorial(c2[V[A-1]])))
