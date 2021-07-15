3
# -*- coding: utf-8 -*-
n, k, c = map(int, input().split())
S = [1 if a == "o" else 0 for a in input()]
count = 0
X = [0] * n
Y = [0] * n
i = 0
while i < n:
    if S[i]:
        count += 1
        X[i] = 1
        i += c + 1
    else:
        i += 1
if count > k:
    return
i = n - 1
while i >= 0:
    if S[i]:
        Y[i] = 1
        i -= c + 1
    else:
        i -= 1
for i in range(0, n):
    if X[i] and Y[i]:
        print(i + 1)
