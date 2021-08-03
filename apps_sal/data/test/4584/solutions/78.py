import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
for i in range(1, n + 1):
    print(c[i])
