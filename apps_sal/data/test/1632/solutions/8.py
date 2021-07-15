from itertools import accumulate

R = lambda: map(int, input().split())
n = int(input())
arr = sorted(R())
ones = [0] * 5005
for i in range(n):
    for j in range(i):
        ones[abs(arr[i] - arr[j])] += 1
twos = [0] * 10005
for i in range(1, 5001):
    for j in range(1, 5001):
        if ones[i] and ones[j]:
            twos[i + j] += ones[i] * ones[j]
stwos = list(accumulate(twos))
sat, sm = 0, 0
for i in range(1, 5001):
    if ones[i]:
        sat += ones[i] * stwos[i - 1]
        sm += ones[i] * stwos[-1]
print(sat / max(1, sm))
