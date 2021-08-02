T = input().split(' ')
n = int(T[0])
w = int(T[1])
S = input().split(' ')
for i in range(len(S)):
    S[i] = int(S[i])
m = 0
M = 0
t = 0
for i in range(len(S)):
    t += S[i]
    M = max(M, t)
    m = min(m, t)
if -m <= w - M:
    print(w - M + m + 1)
else:
    print(0)
