N = int(input())
S = input()

R = ''

rep = 'fox'
nxt = 0
ans = 0
for i in range(N):
    found = False
    for k in range(3):
        if S[i] == rep[k]:
            R += rep[k]
            found = True
    if not found:
        R = ''
    if R[-3:] == rep:
        ans += 1
        R = R[:-3]
print((N-ans*3))

