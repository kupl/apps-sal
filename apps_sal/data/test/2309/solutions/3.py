import sys
from collections import defaultdict
vowel = set([ord(x) for x in ('a', 'e', 'i', 'o', 'u')])
D = {v: i for i, v in enumerate([ord(x) for x in ('a', 'e', 'i', 'o', 'u')])}
N = int(input())
A = defaultdict(list)
B = defaultdict(list)
geta = 10
I = [sys.stdin.readline().strip() for _ in range(N)]
for i, S in enumerate(I):
    S = [ord(x) for x in S]
    p = None
    c = 0
    for s in S[::-1]:
        if s in vowel:
            if p is None:
                p = D[s]
            c += 1
    A[c*geta + p].append(i)
    B[c].append(i)

SA = sum(len(v)//2 for v in A.values())
SB = sum(len(v)//2 for v in B.values())
CA = []
CB = []
used = set()
for v in A.values():
    for i in range(0, len(v)-1, 2):
        CA.append((v[i], v[i+1]))
        used.add(v[i])
        used.add(v[i+1])
for v in B.values():
    fill = True
    T = None
    for i in v:
        if i not in used:
            fill = not fill
            if fill:
                CB.append((T, i))
            else:
                T = i

ans = min(SA, SB//2)
print(ans)
f = min(len(CA), len(CB))
for i in range(f):
    a, b = CA.pop()
    c, d = CB.pop()
    print(I[c], I[a])
    print(I[d], I[b])
for _ in range(ans - f):
    a, b = CA.pop()
    c, d = CA.pop()
    print(I[c], I[a])
    print(I[d], I[b])
