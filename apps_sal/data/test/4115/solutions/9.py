s = list(input())
b = 0
for a in range(int(len(s) / 2)):
    if s[a] != s[len(s) - a - 1]:
        b = b + 1
print(b)
