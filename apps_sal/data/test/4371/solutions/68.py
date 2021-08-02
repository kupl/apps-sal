s = input()
a = 753
for i in range(len(s) - 2):
    b = int(s[i]) * 100 + int(s[i + 1]) * 10 + int(s[i + 2])
    c = abs(753 - b)
    if a > c:
        a = c
        a = abs(a)
print(a)
