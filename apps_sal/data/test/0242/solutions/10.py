import itertools
import bisect
m = int(input())
degs = [0 for i in range(5 * m + 6)]
deg = 5
while deg < 5 * m + 1:
    for i in range(deg, 5 * m + 6, deg):
        degs[i] += 1
    deg *= 5
prefix = list(itertools.accumulate(degs))
i = bisect.bisect_left(prefix, m)
ans = []
for j in range(i, min(i + 5, 5 * m + 6)):
    if prefix[j] == m:
        ans.append(j)
print(len(ans))
for j in ans:
    print(j, end=' ')
