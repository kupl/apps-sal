import itertools as it
n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = [0] + list(it.accumulate(a))
sb = [0] + list(it.accumulate(b))
maxi = 0
j = m
for i in range(n + 1):
    if sa[i] <= k:
        while sa[i] + sb[j] > k:
            j -= 1
        maxi = max(maxi, i + j)

print(maxi)
