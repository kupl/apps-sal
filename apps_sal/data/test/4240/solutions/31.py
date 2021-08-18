S = input()
T = input()

N = len(S)
ans = "No"
for i in range(N):
    if S[-i:] + S[:-i] == T:
        ans = "Yes"
        break

print(ans)
