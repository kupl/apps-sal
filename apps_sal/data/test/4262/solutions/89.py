from itertools import permutations

n = int(input())
P = tuple(map(int, input().split(' ')))
Q = tuple(map(int, input().split(' ')))

l = [i for i in range(1, n+1)]
list = permutations(l)

for i, l in enumerate(list):
    if P==l:
        a = i
    if Q==l:
        b = i
print(abs(a-b))
