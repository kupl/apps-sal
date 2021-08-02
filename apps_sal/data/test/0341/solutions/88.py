N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
G = [[] for n in range(K)]

for n in range(N):
    G[n % K].append(T[n])

cnt = 0
for g in G:
    r, s, p = True, True, True
    for g2 in g:
        if g2 == 'r':
            if p:
                p = False
                r, s = True, True
                cnt += P
            else:
                r, s, p = True, True, True
        if g2 == 's':
            if r:
                r = False
                p, s = True, True
                cnt += R
            else:
                r, s, p = True, True, True
        if g2 == 'p':
            if s:
                s = False
                r, p = True, True
                cnt += S
            else:
                r, s, p = True, True, True

print(cnt)
