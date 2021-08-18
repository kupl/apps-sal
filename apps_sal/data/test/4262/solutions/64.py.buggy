import itertools


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

n = 1
for v in itertools.permutations(list(range(1, N + 1))):
    v = list(v)
    if v == P:
        a = n
    if v == Q:
        b = n
    n += 1

print(abs(a - b))
return
