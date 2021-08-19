N = int(input())
A = list(map(int, input().split()))
Q = int(input())
d = {}
v = 0
ans = []
for a in A:
    d[a] = d.get(a, 0) + 1
    v += a
for i in range(Q):
    (B, C) = list(map(int, input().split()))
    v += d.get(B, 0) * (C - B)
    d[C] = d.get(C, 0) + d.get(B, 0)
    d[B] = 0
    ans.append(v)
for a in ans:
    print(a)
