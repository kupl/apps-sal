n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
origB = list(map(int, input().split()))
b = sorted(origB)
counts = {}
c = 0
i = 0
j = 0
while i < n and j < m:
    if a[i] <= b[j]:
        c = c + 1
        i = i + 1
    else:
        counts[b[j]] = c
        j = j + 1

while j < m:
    counts[b[j]] = c
    j = j + 1

for j in origB:
    print(counts[j], end=' ')
