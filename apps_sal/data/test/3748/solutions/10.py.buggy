# この解法は嘘を含む

from itertools import groupby
H, W = list(map(int, input().split()))
S_ = ["" for _ in range(W)]
T_ = []
for _ in range(H):
    s = input()
    T_.append(s)
    for i, c in enumerate(s):
        S_[i] += c
T = [sorted(t) for t in T_]
S = [sorted(s) for s in S_]
cnt = 0
for _, g in groupby(sorted(T)):
    if len(list(g)) % 2:
        cnt += 1
if H % 2 < cnt:
    print("NO")
    return
cnt = 0
for _, g in groupby(sorted(S)):
    if len(list(g)) % 2:
        cnt += 1
if W % 2 < cnt:
    print("NO")
    return
if W % 2 or H % 2:
    print("YES")
    return
T1 = []
T2 = []
for i, (_, t) in enumerate(sorted(zip(T, T_))):
    if i % 2:
        T1.append(t)
    else:
        T2.append(t)
T_p = T1 + T2[::-1]
S_pp = ["" for _ in range(W)]
for t in T_p:
    for i, c in enumerate(t):
        S_pp[i] += c
S1 = []
S2 = []
for i, (_, s) in enumerate(sorted(zip(S, S_pp))):
    if i % 2:
        S1.append(s)
    else:
        S2.append(s)
S_p = S1 + S2[::-1]
for s1, s2 in zip(S_p, S_p[::-1]):
    for c1, c2 in zip(s1, s2[::-1]):
        if c1 != c2:
            print("NO")
            return
print("YES")
