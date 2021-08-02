n = int(input())
s = input()
t = str()
for i in range(len(s)):
    if ord(s[i]) + n <= 90:
        t += chr(ord(s[i]) + n)
    else:
        t += chr(ord(s[i]) + n - 26)
print(t)
