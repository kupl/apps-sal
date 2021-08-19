n = int(input())
a = [int(x) - 1 for x in input().split()]
counts = [0] * 10
for (ind, i) in enumerate(a):
    counts[i] += 1
    k = sorted([i for i in counts if i])
    if len(k) == 1 or (k[0] == k[-2] and k[-1] - k[-2] == 1) or (k[0] == 1 and k[1] == k[-1]):
        best = ind
print(best + 1)
