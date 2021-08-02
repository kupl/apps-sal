n = int(input())
s = list(str(input()))
for i in range(len(s)):
    ns = ord(s[i]) - 64
    print(chr((ns + n - 1) % 26 + 65), end='')
