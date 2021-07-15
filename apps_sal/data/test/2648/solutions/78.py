from collections import defaultdict
n = int(input())
a_list = [int(x) for x in input().split()]
d = defaultdict(int)
for a in a_list:
    d[a] += 1
print(len(d.keys()) - sum([1 - v % 2 for v in d.values()]) % 2)
