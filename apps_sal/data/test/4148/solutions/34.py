n = int(input())
s = list(input())
ans = ''

for i in s:
    ascii_code = (ord(i) + n)
    if ascii_code >= 91:
        ascii_code -= 26

    ans += chr(ascii_code)

print(ans)
