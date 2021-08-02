from functools import reduce
n, k = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
tmp_max = sum([i / 2 + 0.5 for i in p[0:k]])
tmp = tmp_max
idx = 0
for i in range(1, len(p) - k + 1):
    tmp -= p[i - 1] / 2 + 0.5
    if i + k - 1 < len(p):
        tmp += p[i + k - 1] / 2 + 0.5
    tmp_max = max(tmp_max, tmp)
print(tmp_max)
