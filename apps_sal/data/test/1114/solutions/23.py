# import sys
# sys.stdin = open('cf599b.in')

from collections import Counter

n, m = map(int, input().split())

ff = list(map(int, input().split()))
df = {int(v): i for i, v in enumerate(ff, 1)}
cnt = Counter(ff)

bb = list(map(int, input().split()))

try:
    ans = ' '.join(str(df[b]) for b in bb)
    if any(cnt[b] > 1 for b in bb):
        print('Ambiguity')
    else:
        print('Possible')
        print(ans)
except KeyError:
    print('Impossible')
