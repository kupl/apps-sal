n = input()
m = input()
N = {}
for c in n:
    if c in N:
        N[c] += 1
    else:
        N[c] = 1
M = {}
for c in m:
    if c in M:
        M[c] += 1
    else:
        M[c] = 1
S = 0
for (color, count) in list(M.items()):
    if color not in N:
        S = -1
        break
    else:
        S += min(count, N[color])
print(S)
