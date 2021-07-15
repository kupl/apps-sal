import itertools, math
N = int(input())
ls, L = [], 0
for i in range(N):
    x, y = map(int, input().split(' '))
    ls.append([x, y])
perms = itertools.permutations(range(N))
for perm in perms:
    for i in range(N - 1):
        L += math.sqrt((ls[perm[i + 1]][0] - ls[perm[i]][0]) ** 2 + (ls[perm[i + 1]][1] - ls[perm[i]][1]) ** 2)
print(L / math.factorial(N))
