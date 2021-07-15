n = int(input())
s = list(map(str, input().split()))
import collections
s = collections.Counter(s)
if len(s.keys()) == 3:
    print("Three")
else:
    print("Four")
