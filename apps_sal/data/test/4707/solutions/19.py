s = list(input())
ans = 0
for i in range(len(s)):
    if s[i] == '1':
        ans += 1
else:
    print(ans)
