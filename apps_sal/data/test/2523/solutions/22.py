import numpy as np
S = str(input())
X = []
c = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        c += 1
    elif S[i] != S[i - 1]:
        X += [c]
        c = 1
    if i == len(S) - 1:
        X += [c]
if len(S) == 1:
    X = [1]
if len(X) >= 3:
    X = np.cumsum(X)
    t = float('inf')
    for i in range(len(X) - 1):
        u = max(X[i], len(S) - X[i])
        t = min(u, t)
    answer = t
elif len(X) == 1:
    answer = X[0]
elif len(X) == 2:
    answer = max(X)
print(answer)
