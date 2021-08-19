s = input()
b = 0
w = 0
for i in range(len(s)):
    if s[i] == '0':
        b = b + 1
    if s[i] == '1':
        w = w + 1
print(2 * min(b, w))
