S = sorted(list(input()))
p = len(S) // 2
g = len(S) // 2
if len(S) % 2 == 1:
    g += 1
T = ['g'] * g + ['p'] * p
ans = 0
for i in range(len(S)):
    if T[i] == 'g' and S[i] == 'p':
        ans -= 1
    if T[i] == 'p' and S[i] == 'g':
        ans += 1
print(ans)
