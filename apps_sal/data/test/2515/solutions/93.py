from itertools import accumulate

q, *lr = list(map(int, open(0).read().split()))

p = [True] * 100010
p[0] = False
p[1] = False
i = 2
while i <= 100005:
    if p[i]:
        j = i * 2
        while j <= 100005:
            p[j] = False
            j += i
    i += 1

s = [0] * 100010
for i in range(3, 100005, 2):
    if p[i] and p[(i + 2) // 2]:
        s[i] += 1
s = tuple(accumulate(s))

for l, r in zip(*[iter(lr)] * 2):
    print((s[r] - s[l - 1]))
