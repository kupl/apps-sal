n, k = map(int, input().split())
s = [int(i) for i in input()]
l1, l0 = [], []
b, c = 1, 0
for i in s:
    if b == i: c += 1
    else:
        if b: l1 += [c]
        else: l0 += [c]
        c = 1
    b = i
if b:
    l1 += [c]
    l0 += [0]
else:
    l0 += [c]
S = [0]
for i, j in zip(l1, l0):
    S += [S[-1] + i + j]
l1 += [0]
m = len(S)
if m <= k:
    print(n)
    return
a = 0
for i in range(k, m):
    a = max(a, S[i] - S[i - k] + l1[i])
print(a)
