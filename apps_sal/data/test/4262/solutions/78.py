import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
p = list(itertools.permutations(range(1, N + 1)))
(a, b) = [0, 0]
for (i, pair) in enumerate(p, 1):
    if P == pair:
        a = i
    if Q == pair:
        b = i
print(abs(a - b))
