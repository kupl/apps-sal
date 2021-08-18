from collections import defaultdict, Counter
n = int(input())
a = defaultdict(list)
count_left = Counter()
count_right = Counter()

for _ in range(n):
    l, r = map(int, input().split())
    count_left[l] += 1
    count_right[r] += 1

count = [0] * (n + 1)


pts = sorted(set(count_left.keys()) | set(count_right.keys()))
c = 0
prev = pts[0]
for pt in pts:
    if count_left[pt]:
        count[c] += pt - prev - 1
        c += count_left[pt]
        count[c] += 1
        c -= count_right[pt]
    else:
        count[c] += pt - prev
        c -= count_right[pt]

    prev = pt

print(' '.join(map(str, count[1:])))
