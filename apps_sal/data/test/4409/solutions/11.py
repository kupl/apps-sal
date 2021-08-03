from collections import Counter
n = int(input())
a = list(map(int, input().split()))


def compute_mode(numbers):
    counts = Counter(numbers)
    maxcount = max(counts.values())
    for num, count in counts.items():
        if count == maxcount:
            return num


m = compute_mode(a)
mi = a.index(m)
k = []

for i in range(mi - 1, -1, -1):
    if a[i] > m:
        k.append([2, i + 1, i + 2])
    elif a[i] < m:
        k.append([1, i + 1, i + 2])
for i in range(mi + 1, n):
    if a[i] > m:
        k.append([2, i + 1, i])
    elif a[i] < m:
        k.append([1, i + 1, i])
print(len(k))
for i in k:
    print(*i)
