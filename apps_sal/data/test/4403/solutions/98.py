S = str(input())
N = len(S)
ans = 0
for i in range(N):
    if S[i] == "+":
        ans += 1
    else:
        ans -= 1
print(ans)
