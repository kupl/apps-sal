S = input()
N = len(S)
ans = 0
if S[0] == '0':
    for i in range(1, N):
        if i % 2 == 0 and S[i] == '1':
            ans += 1
        if i % 2 == 1 and S[i] == '0':
            ans += 1
else:
    for i in range(1, N):
        if i % 2 == 0 and S[i] == '0':
            ans += 1
        if i % 2 == 1 and S[i] == '1':
            ans += 1
print(ans)
