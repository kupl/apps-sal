import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

a = b = -1
for i, x in enumerate(itertools.permutations(range(1, n + 1))):
    if x == p:
        a = i
    if x == q:
        b = i

print(abs(a - b))
