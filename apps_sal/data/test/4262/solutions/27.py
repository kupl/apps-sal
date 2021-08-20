import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
L = [i for i in range(1, N + 1)]
K = list(itertools.permutations(L))
K.sort()
(p, q) = (0, 0)
for i in range(len(K)):
    if list(K[i]) == P:
        p = i
    if list(K[i]) == Q:
        q = i
print(abs(p - q))
