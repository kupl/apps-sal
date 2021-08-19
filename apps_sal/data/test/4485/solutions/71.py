from collections import defaultdict
N, M = [int(x) for x in input().split()]
dict = defaultdict(bool)  # int/bool/list....
for i in range(M):
    a, b = [int(x) for x in input().split()]
    dict[(a, b)] = True

for j in range(1, N + 1):
    if dict[(1, j)] and dict[(j, N)]:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')
