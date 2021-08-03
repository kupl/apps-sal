import collections as c
n = int(input())
t = c.Counter(map(int, input().split()))
for i in range(1, n + 1):
    print([0, t[i]][i in t])
