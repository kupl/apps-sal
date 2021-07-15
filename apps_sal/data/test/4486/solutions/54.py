s = input()
x = ''
for i in range(0, len(s)):
    if i % 2 == 0:
        x = x + s[i]
print(x)
