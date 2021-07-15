n = int(input())
s = input()
ans = ''
for i in range(len(s)):
    if ord(s[i])+n>90:
        ans  += chr(ord(s[i])+n-26)
    else:
        ans  += chr(ord(s[i])+n)
print(ans)
