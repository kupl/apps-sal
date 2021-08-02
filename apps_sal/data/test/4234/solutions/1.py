n = int(input())
s = input().strip()

a = ''
for i in range(n):
    if len(a) < 2 or a[-2:] != s[i] * 2:
        a += s[i]

b = ''
for i in range(len(a)):
    if len(b) & 1:
        if a[i] != b[-1]:
            b += a[i]
    else:
        b += a[i]

if len(b) & 1:
    b = b[:-1]
print(n - len(b))
print(b)
