s = input()
cau = 0
l = len(s)
for j in range(l // 2 + l % 2):
    if s[j] != s[-1 - j]:
        cau = cau + 1
print(cau)
