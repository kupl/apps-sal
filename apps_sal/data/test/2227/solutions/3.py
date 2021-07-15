s = input().strip()
ans = 0
head = 0
for i in range(4, len(s)):
    if s[i - 4: i + 1] == "heavy":
        head += 1
    if s[i - 4: i + 1] == 'metal':
        ans += head
print(ans)

