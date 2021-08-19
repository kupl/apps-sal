import bisect
n = int(input())
V = sorted([int(x) for x in input().split()])
cont = 0
pot = 2
for i in range(1, n):
    while pot <= V[i]:
        pot *= 2
    indL = bisect.bisect_left(V, pot - V[i], 0, i)
    indR = bisect.bisect_right(V, pot - V[i], 0, i)
    cont += indR - indL
print(cont)
