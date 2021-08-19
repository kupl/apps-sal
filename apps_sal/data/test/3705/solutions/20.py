import collections
n = int(input())
s = input()
c = collections.Counter(s)
print(min(c['8'], len(s) // 11))
