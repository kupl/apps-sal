n = int(input())
l = list(map(int, input().split(' ')))
idxs = sorted(list(range(n)), key=lambda x: l[x])
for i in range(1, n):
    if l[idxs[i]] <= l[idxs[i - 1]]:
        l[idxs[i]] = l[idxs[i - 1]] + 1
print(' '.join(map(str, l)))
