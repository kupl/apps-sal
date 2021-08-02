N = int(input())
S = input()

e_all = S.count('E')

w_cnt = 0
e_cnt = 0
ans = float('inf')
for i in range(N):
    if S[i] == 'W':
        w_cnt += 1
        ans = min(ans, w_cnt - 1 + e_all - e_cnt)
    else:
        e_cnt += 1
        ans = min(ans, w_cnt + e_all - e_cnt)

print(ans)
