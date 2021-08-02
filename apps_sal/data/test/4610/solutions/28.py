import collections as c
n, k = map(int, input().split()); a = c.Counter(map(int, input().split()))
print([0, sum(sorted([i for i in a.values()])[:len(a) - k])][len(a) > k])
