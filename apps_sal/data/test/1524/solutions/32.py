S = str(input())
l = len(S)
d = [0] * l

R, L = 0, 0
for i in range(l):
    if S[i] == 'R':
        R += 1
        if R == 1 and L > 0:
            L -= 1
            p = L // 2
            d[i - L - 2] += L - p  # R
            d[i - L - 1] += p  # L
            L = 0
    else:
        L += 1
        if R > 0 and L == 1:
            R -= 1
            p = R // 2
            d[i - 1] += p + 1  # R
            d[i] += R - p + 1  # L
            R = 0
if L > 1:
    L -= 1
    p = L // 2
    d[-L - 2] += L - p
    d[-L - 1] += p
print(*d)
