s = input()
l = len(s)
for i in range(l - 2):
    if s[i] == s[i + 1]:
        print(i + 1, i + 2)
        break
    if s[i] == s[i + 2]:
        print(i + 1, i + 3)
        break
else:
    if s[-2] == s[-1]:
        print(l - 1, l)
    else:
        print(-1, -1)
