N = int(input())
S = list(input())
ans = 0
n_ans = 0
for i in range(N):
    if S[i] == 'I':
        n_ans += 1
        ans = max(ans, n_ans)
    else:
        n_ans -= 1
        ans = max(ans, n_ans)
print(ans)
