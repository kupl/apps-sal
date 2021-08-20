s = input()
a = -1
b = -1
for i in range(len(s) - 2):
    if s[i] == s[i + 1]:
        a = i + 1
        b = i + 2
    elif s[i] == s[i + 2]:
        a = i + 1
        b = i + 3
if s[-1] == s[-2]:
    a = len(s) - 1
    b = len(s)
print(a, b)
