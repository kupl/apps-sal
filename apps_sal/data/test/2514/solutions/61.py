from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = defaultdict(int)
v = 0
ans = []

for a in A:
    d[a] += 1
    v += a

for i in range(Q):
    B, C = list(map(int, input().split()))
    v += d[B] * (C - B)
    d[C] += d[B]
    d[B] = 0
    ans.append(v)

for a in ans:
    print(a)
