N = int(input())
S = list(input())
E = S[1:].count('E')
W = 0
mi = E + W
for i in range(1, N):
    if S[i] == 'E':
        E -= 1
    if S[i - 1] == 'W':
        W += 1
    if E + W <= mi:
        mi = E + W
print(mi)
