import collections
import itertools
N = int(input())
S = [input() for _ in range(N)]
S = [s[0] for s in S if s[0] == 'M' or s[0] == 'A' or s[0] == 'R' or s[0] == 'C' or s[0] == 'H']

cnt = collections.Counter(S)

comb = itertools.combinations(cnt.keys(), 3)

ans = 0
for a, b, c in comb:
    ans += cnt[a] * cnt[b] * cnt[c]
print(ans)
