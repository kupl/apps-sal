
import collections
n, m = map(int, input().split())
a = collections.Counter(list(map(int, input().split())))
if len(a) < n:
    print(0)
else:
    print(min(a.values()))
