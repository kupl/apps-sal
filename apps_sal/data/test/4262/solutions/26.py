from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

for i, p in enumerate(permutations(list(range(1, N+1)))):
    if p == P:
        a = i
    if p == Q:
        b = i
print((abs(a-b)))

