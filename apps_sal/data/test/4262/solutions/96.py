from itertools import permutations
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
c = list(permutations([i for i in range(1, n + 1)], n))
print(abs(c.index(p) - c.index(q)))
