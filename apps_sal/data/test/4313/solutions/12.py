import itertools
N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
diff_VC = list(i - j for i, j in zip(V, C))
c = []
for i in range(N):
    c += [sum(comb) for comb in itertools.combinations(diff_VC, i + 1)]
print(max(max(c), 0))
