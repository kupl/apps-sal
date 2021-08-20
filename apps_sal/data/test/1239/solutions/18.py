n = int(input())
a = sorted(map(int, input().split()))
count = 0
best = 2 * 10 ** 9 + 1
for (s1, s2) in zip(a, a[1:]):
    d = abs(s1 - s2)
    if d == best:
        count += 1
    elif d < best:
        count = 1
        best = d
print(best, count)
