N = int(input())
S = input()

R = ''

rep = 'fox'
nxt = 0
ans = 0
for i in range(N):
    R += S[i]
    if len(R) >= 3 and R[-3:] == rep:
        R = R[:-3]

print((len(R)))

