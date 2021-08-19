n = int(input())
a = [int(t) for t in input().split()]
counts = dict()
for num in a:
    counts[num] = counts.setdefault(num, 0) + 1
m = max(counts)
pows = [2]
while pows[-1] < m:
    pows.append(2 * pows[-1])
pows.append(2 * pows[-1])
total = 0
for a in counts:
    matchesFora = 0
    for p in pows:
        if p - a in counts:
            matchesFora += counts[p - a]
            if p - a == a:
                matchesFora -= 1
    total += matchesFora * counts[a]
total //= 2
print(total)
