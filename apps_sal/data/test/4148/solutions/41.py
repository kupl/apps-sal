n = int(input())
s = input()
ans = []
for i in range(len(s)):
    num = ord(s[i]) + n
    if num > 90:
        num -= 26
    ans.append(chr(num))
ans = ''.join(ans)
print(ans)
