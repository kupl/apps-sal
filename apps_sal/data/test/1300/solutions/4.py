from collections import defaultdict
n, tar = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

d = defaultdict(lambda: [])
count = 0
for i in range(n):
    d[a[i]].append(i)
    if a[i] == tar:
        count += 1

presum = [1 if a[0] == tar else 0]
for e in a[1:]:
    if e == tar:
        presum.append(presum[-1] + 1)
    else:
        presum.append(presum[-1])

final = 0
for k, v in d.items():
    if k == tar:
        continue

    t = 1
    tt = 1
    for i in range(1, len(v)):
        ind = v[i]
        preind = v[i - 1]

        t -= presum[ind] - presum[preind]
        t = max(t, 0)
        t += 1
        tt = max(tt, t)

    final = max(final, tt)

print(final + count)
