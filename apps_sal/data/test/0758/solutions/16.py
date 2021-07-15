n = int(input())
s = input()
ans = 0
for i in range(len(s)):
    ch = s[i]
    if ch == 'B':
        ans |= 1 << i
print(ans)
