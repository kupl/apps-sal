N = int(input())
S = str(input())
ans = 1
s = list(map(str, str(S)))

for i in range(N - 1):
    if s[i] != s[i + 1]:
        ans += 1
print(ans)
