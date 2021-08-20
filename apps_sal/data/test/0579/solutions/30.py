from itertools import accumulate
import sys
sys.setrecursionlimit(10 ** 8)
(n, k) = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
p = [i - 1 for i in p]
seen = [False] * n
ans = -float('inf')
for i in range(n):
    if not seen[i]:
        sc = []
        stop = i
        while True:
            seen[i] = True
            sc.append(c[i])
            if p[i] == stop:
                break
            i = p[i]
        lens = len(sc)
        for j in range(lens):
            if j != 0:
                sc = sc[1:] + [sc[0]]
            ac = list(accumulate(sc))
            if sum(sc) <= 0:
                ans = max(ans, max(ac[:min(k, lens)]))
            elif k % lens == 0:
                ans = max(ans, ac[-1] * (k // lens - 1) + max(ac))
            else:
                ans = max(ans, ac[-1] * (k // lens) + max(ac[:k % lens]))
print(ans)
