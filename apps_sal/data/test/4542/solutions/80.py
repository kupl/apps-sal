s = input()
prev = s[0]
ans = 0
for i in range(1, len(s)):
    if s[i] != prev:
        ans += 1
    prev = s[i]
print(ans)
