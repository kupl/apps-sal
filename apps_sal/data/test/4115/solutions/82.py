S = input()
dis = len(S) - 1
ans = 0
for i in range(len(S) // 2):
    if S[i] != S[dis]:
        ans += 1
    dis -= 1
print(ans)
