S = input()
ans = 0
for i in range(len(S)):
    if S[i] != S[-1 * (i + 1)]:
        ans += 1
print(ans // 2)
