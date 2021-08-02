s = input()
n = len(s)
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        print((i, i + 1))
        break
    elif i > 1 and s[i - 2] == s[i]:
        print((i - 1, i + 1))
        break
else:
    print((-1, -1))
