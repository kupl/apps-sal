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
for num in a:
    for p in pows:
        if p - num in counts:
            total += counts[p - num]
            if p - num == num:
                total -= 1
total //= 2
print(total)
