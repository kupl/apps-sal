with open(0) as f:
    N, S = f.read().split()
N = int(N)
S += '_'
left = 0
right = 0
cnt = 0
for i in range(N):
    cnt += {'(':1, ')':-1}[S[i]]
    if S[i] == ')' and S[i+1] != ')':
        if cnt < 0:
            left += -cnt
            cnt = 0
    if i == N-1 and cnt > 0:
        right += cnt
ans = '(' * left + S[:N] + ')' * right
print(ans)
