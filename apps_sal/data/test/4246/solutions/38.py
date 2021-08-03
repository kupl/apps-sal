s = list(input())
t = list(input())
ans = 0
for i in range(3):
    if s[i] == t[i]:
        ans += 1
print(ans)
