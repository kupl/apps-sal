s = input()
i1 = -1
i2 = -1
k1 = -1
k2 = -1
c = 0
for i in range(len(s)):
    if s[i] == '[':
        i1 = i
        break
for i in range(len(s) - 1, -1, -1):
    if s[i] == ']':
        i2 = i
        break
for i in range(i1, i2 + 1):
    if s[i] == ':':
        k1 = i
        break
for i in range(i2, i1 - 1, -1):
    if s[i] == ':':
        k2 = i
        break
for i in range(k1, k2 + 1):
    if s[i] == '|':
        c += 1
if i1 == -1 or i2 == -1 or i1 >= i2 or (k1 == -1) or (k2 == -1) or (k1 == k2):
    print(-1)
else:
    print(4 + c)
