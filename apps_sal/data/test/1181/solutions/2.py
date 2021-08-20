(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = {}
for ai in a:
    b[ai] = []
amt = 0
for i in range(1, len(a)):
    amt += abs(a[i] - a[i - 1])
    if a[i] - a[i - 1]:
        b[a[i]] += [a[i - 1]]
        b[a[i - 1]] += [a[i]]
diff = 0
for bi in b:
    if b[bi]:
        center = sorted(b[bi])[len(b[bi]) // 2]
        sum = 0
        for page in b[bi]:
            sum += abs(page - center) - abs(page - bi)
        diff = min(diff, sum)
print(amt + diff)
