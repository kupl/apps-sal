import copy
n = int(input())
A = list(map(int, input().split()))
L = [0] * n

for x in A:
    L[x - 1] += 1
for i in L:
    print(i)
