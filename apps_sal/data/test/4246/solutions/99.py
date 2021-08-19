ans = 0
S = input()
T = input()
for i in range(3):
    if S[i] == T[i]:
        ans += 1
print(ans)
