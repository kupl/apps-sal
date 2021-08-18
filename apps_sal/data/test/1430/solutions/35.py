N, K = list(map(int, input().split()))
S = input()

S = S + 'E'
ans = -1

if (S[0] == '0'):
    stand = 1
else:
    stand = 0

L = 0
R = 0

while (R < N):
    if (stand <= K):
        if (S[R] == '1' and S[R + 1] == '0'):
            stand += 1
        ans = max(ans, R - L + 1)
        R += 1
    elif (L == R):
        L += 1
        R += 1
    else:
        if (S[L] == '0' and S[L + 1] == '1'):
            stand -= 1
        L += 1

print(ans)
