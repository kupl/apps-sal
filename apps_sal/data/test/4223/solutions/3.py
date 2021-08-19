N = int(input())
S = str(input())
ans = 1
for i in range(1, N):
    if S[i] == S[i - 1]:
        continue
    else:
        ans += 1
print(ans)
