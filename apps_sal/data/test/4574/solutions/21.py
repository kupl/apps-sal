n = int(input())
A = tuple(map(int, input().split()))
A = sorted(A, reverse=True)
from collections import Counter
CA = Counter(A)

b = 0
for a in A:
    if CA[a] >= 2:
        CA[a] -= 2
        b = a
        break

c = 0
for a in A:
    if CA[a] >=2:
        c = a
        break
print((b*c))

