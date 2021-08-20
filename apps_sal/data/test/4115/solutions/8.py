s = list(input())
ans = 0
r = list(reversed(s))
for i in range(len(s) // 2):
    if s[i] != r[i]:
        ans += 1
print(ans)
