import itertools

L = list(map(int, input().split()))
total = sum(L)

for i in range(1, 4):
    for comb in itertools.combinations(L, i):
        if sum(comb) == total - sum(comb):
            print('Yes')
            return
print('No')
