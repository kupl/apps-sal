s = input()
c = 0
l = len(s)
for i in range(l // 2):
    if s[i] != s[l - i - 1]:
        c += 1
print(c)
