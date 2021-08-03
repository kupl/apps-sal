import collections
n = int(input())
s = list(map(str, input().split()))
s = collections.Counter(s)
if len(s.keys()) == 3:
    print("Three")
else:
    print("Four")
