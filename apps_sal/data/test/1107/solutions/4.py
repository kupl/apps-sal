n = int(input())
s = input()
ans = 0
for i in range(len(s)):
    if i % n == 0 and i >= 3:
        if s[i - 1] == s[i - 2] == s[i - 3]:
            ans += 1
print(ans)
