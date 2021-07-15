s = input()
for i in range(len(s)):
    if (s[i] != s[-i - 1]):
        print(len(s))
        break
else:
    for i in s:
        if (i != s[0]):
            print(len(s) - 1)
            break
    else:
        print(0)
