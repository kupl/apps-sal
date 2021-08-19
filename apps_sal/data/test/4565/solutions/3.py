N = int(input())
S = list(input())
ans_list = []
ans = S[1:].count('E')
ans_list.append(ans)
for i in range(1, N):
    if S[i - 1] == 'W':
        ans += 1
    if S[i] == 'E':
        ans -= 1
    ans_list.append(ans)
print(min(ans_list))
