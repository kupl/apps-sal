S = str(input())
l = len(S)
d = [0] * l
(R, L) = (0, 0)
(R_flag, L_flag) = (0, 0)
for i in range(l):
    if S[i] == 'R':
        R_flag = 1
        R += 1
        if R == 1 and L > 0:
            L -= 1
            p = L // 2
            d[i - L - 2] += L - p
            d[i - L - 1] += p
            L = 0
    else:
        L_flag = 1
        L += 1
        if R > 0 and L == 1:
            R -= 1
            p = R // 2
            d[i - 1] += p + 1
            d[i] += R - p + 1
            R = 0
if L > 1 and R_flag == 1:
    L -= 1
    p = L // 2
    d[-L - 2] += L - p
    d[-L - 1] += p
print(*d)
