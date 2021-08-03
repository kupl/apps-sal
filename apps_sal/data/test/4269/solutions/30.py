S = input()

ans = "Good"
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        ans = "Bad"

print(ans)
