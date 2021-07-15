import sys
s = input()
ans = ''
for i in range(len(s)):
    ans+=s[i]
print(ans+ans[::-1])
