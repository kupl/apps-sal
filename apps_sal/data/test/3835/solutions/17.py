import math

n = int(input())
prod = [[int(tok) for tok in input().split()] for _ in range(n)]

prod3 = int(math.sqrt(prod[0][1] * prod[0][2] * prod[1][2]))
first = prod3 // prod[1][2]

print(first, end = " ")
for i in range(1, n):
    print(prod[0][i] // first, end = " ")
print()

