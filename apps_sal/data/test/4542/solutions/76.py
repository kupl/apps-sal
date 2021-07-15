s = input()
ans = 0
x = s[0]

for i in range(len(s)):
    if s[i] != x:
        ans += 1
        x = s[i]

print(ans)
