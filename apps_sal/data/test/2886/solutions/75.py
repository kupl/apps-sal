s = input()
n = len(s)
a = b = -1
for i in range(n - 1):
    if s[i] == s[i + 1]:
        (a, b) = (i + 1, i + 2)
        break
    elif i + 2 < n and s[i] == s[i + 2]:
        (a, b) = (i + 1, i + 3)
        break
print((a, b))
