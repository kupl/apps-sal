N = int(input())
S = input()
all = S.count('R') * S.count('G') * S.count('B')
cnt = 0
for i in range(N):
    for j in range(i, N):
        k = 2 * j - i
        if k >= N:
            continue
        if S[i] != S[j] and S[i] != S[k] and (S[j] != S[k]):
            cnt += 1
print(all - cnt)
