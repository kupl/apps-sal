(N, K) = list(map(int, input().split()))
(R, S, P) = list(map(int, input().split()))
T = input()
w1 = ''
w2 = ''
ans = 0
for i in range(N):
    if T[i] == 'r':
        w1 += 'p'
    elif T[i] == 'p':
        w1 += 's'
    else:
        w1 += 'r'
for i in range(0, K):
    if T[i] == 'r':
        w2 += 'p'
        ans += P
    elif T[i] == 'p':
        w2 += 's'
        ans += S
    else:
        w2 += 'r'
        ans += R
if N >= 2:
    for i in range(K, N):
        if w1[i] == w2[i - K]:
            w2 += '_'
        elif w1[i] == 'p':
            w2 += 'p'
            ans += P
        elif w1[i] == 's':
            w2 += 's'
            ans += S
        else:
            w2 += 'r'
            ans += R
print(ans)
