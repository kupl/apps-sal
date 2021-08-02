import itertools
N = int(input())
L = map(int, input().split())
count = 0
for i, j, k in list(itertools.combinations(L, 3)):
    if (i != j and j != k and i != k) and (i + j > k and i + k > j and j + k > i):
        count += 1
print(count)
