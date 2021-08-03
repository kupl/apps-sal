import itertools
N = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
n = tuple(itertools.permutations([i for i in range(1, N + 1)]))
ans = abs(n.index(p) - n.index(q))
print(ans)
