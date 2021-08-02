from itertools import permutations
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
P = sorted(list(permutations(range(1, n + 1), n)))
print(abs(P.index(p) - P.index(q)))
