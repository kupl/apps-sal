N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ans = 0
chk = [0] * N
for n in range(N):
    c = T[n]
    if n >= K and T[n - K] == c and chk[n - K] == 0:
        chk[n] = 1  # not used
        continue
    if c == 'r':
        ans += P
    elif c == 's':
        ans += R
    else:
        ans += S

print(ans)
