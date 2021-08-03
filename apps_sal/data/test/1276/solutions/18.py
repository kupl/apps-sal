N = int(input())
S = list(input())

r = S.count('R')
g = S.count('G')
b = S.count('B')

cnt = 0
for i in range(N - 3):
    if S[i] == 'R':
        r -= 1
        cnt += g * b
        l = 1
        while (i + 2 * l < N):
            if (S[i + l] == 'G' and S[i + 2 * l] == 'B') or (S[i + l] == 'B' and S[i + 2 * l] == 'G'):
                cnt -= 1
            l += 1
    if S[i] == 'G':
        g -= 1
        cnt += r * b
        l = 1
        while (i + 2 * l < N):
            if (S[i + l] == 'R' and S[i + 2 * l] == 'B') or (S[i + l] == 'B' and S[i + 2 * l] == 'R'):
                cnt -= 1
            l += 1
    if S[i] == 'B':
        b -= 1
        cnt += g * r
        l = 1
        while (i + 2 * l < N):
            if (S[i + l] == 'G' and S[i + 2 * l] == 'R') or (S[i + l] == 'R' and S[i + 2 * l] == 'G'):
                cnt -= 1
            l += 1
print(cnt)
