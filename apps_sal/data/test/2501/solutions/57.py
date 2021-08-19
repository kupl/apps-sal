import collections
N = int(input())
A = list(map(int, input().split()))
s = 0
d = collections.defaultdict(int)
for i in range(N):
    d[i + A[i]] += 1
for i in range(N):
    s += d[i - A[i]]
print(s)
