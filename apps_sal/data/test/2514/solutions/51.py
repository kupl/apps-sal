import numpy as np
n = int(input())
li_a = list(map(int, input().split()))
A = [0] * (10**5)
s = sum(li_a)

li_a = list(map(lambda x: x - 1, li_a))
for a in li_a:
    A[a] += 1
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    if A[b - 1] > 0:
        A[c - 1] += A[b - 1]
        s -= b * A[b - 1]
        s += c * A[b - 1]
        A[b - 1] = 0
        print(s)
    else:
        print(s)
