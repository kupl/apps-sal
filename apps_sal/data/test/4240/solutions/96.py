S = input() * 2
T = input()
N = len(T)
for i in range(N):
    if T == S[i:N + i]:
        ans = "Yes"
        break
else:
    ans = "No"
print(ans)
