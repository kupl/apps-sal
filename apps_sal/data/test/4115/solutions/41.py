S = input()
T = ''.join([S[i] for i in range(len(S) - 1, -1, -1)])
ans = 0
for i in range(len(S) // 2):
    if S[i] != T[i]:
        ans += 1
print(ans)
