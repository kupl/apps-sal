from collections import defaultdict as dd, deque, Counter

n,m = list(map(int,input().split()))

A = [input() for _ in range(n)]
P = [int(x) for x in input().split()]

r = 0
for a in zip(list(zip(*A)), P):
    c = Counter(a[0])
    r += c.most_common()[0][1]*a[1]
print(r)

