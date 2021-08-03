import sys
input = sys.stdin.readline

n = int(input())
S = input().strip()

mod = 10**9 + 7

A = 0
AB = 0
ABC = 0
q = 0

for s in S:
    if s == "a":
        A += pow(3, q, mod)
    elif s == "b":
        AB += A
    elif s == "c":
        ABC += AB
    else:
        ABC = AB + ABC * 3
        AB = A + AB * 3
        A = pow(3, q, mod) + A * 3
        q += 1
    A %= mod
    AB %= mod
    ABC %= mod

print(ABC)
