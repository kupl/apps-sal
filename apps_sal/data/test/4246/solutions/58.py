S = input()
T = input()

ans = 0
if S[0] == T[0]:
    ans += 1
if S[1] == T[1]:
    ans += 1
if S[2] == T[2]:
    ans += 1

print(ans)
