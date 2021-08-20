import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
i = 1
a = 0
b = 0
for l in itertools.permutations(list(range(1, N + 1))):
    if ''.join([str(n) for n in P]) == ''.join([str(n) for n in l]):
        a = i
    if ''.join([str(n) for n in Q]) == ''.join([str(n) for n in l]):
        b = i
    i += 1
print(abs(a - b))
