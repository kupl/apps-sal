import sys

t = int(input())

for _ in range(t):
    L, v, l, r = list(map(int, input().split()))
    n1 = (l - 1) // v
    n2 = r // v
    print(L // v - (n2 - n1))
