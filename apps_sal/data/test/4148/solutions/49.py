import string
abc = list(string.ascii_uppercase)

n = int(input())
s = list(input())

for i in range(len(s)):
    x = abc.index(s[i])
    s[i] = abc[(x + n) % 26]
print((''.join(s)))
