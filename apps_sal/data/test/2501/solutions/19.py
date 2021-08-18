import collections
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

l = [j - aj for j, aj in enumerate(a, 1)]
r = [i + ai for i, ai in enumerate(a, 1)]
cnt = collections.Counter(r)
ans = 0
for i in l:
    ans += cnt[i]
print(ans)
