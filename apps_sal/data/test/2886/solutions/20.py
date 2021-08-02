s = input() + "_"
x = y = -2
for i in range(len(s) - 2):
    if s[i] == s[i + 1]:
        x = i; y = i + 1
    if s[i] == s[i + 2]:
        x = i; y = i + 2
print(x + 1, y + 1)
