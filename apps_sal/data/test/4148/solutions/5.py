n = int(input())
s = list(str(input()))
a = ''
for i in s:
    b = (ord(i) + n - 65) % 26
    a += chr(b + 65)
print(a)
