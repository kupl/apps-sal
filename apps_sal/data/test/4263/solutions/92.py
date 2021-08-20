S = input()
S = list(S)
for i in range(len(S)):
    s = S[i]
    if (s == 'A') | (s == 'T') | (s == 'C') | (s == 'G'):
        S[i] = 0
    else:
        S[i] = 1
point = [0] * (len(S) + 1)
for i in range(0, len(S)):
    if S[i] == 0:
        point[i + 1] = point[i] + 1
    else:
        point[i + 1] = 0
print(max(point))
