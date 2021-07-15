s = input()
l = len(s)
for i in range(l - 1):
    if s[i] == s[i + 1]:
        print(i + 1, i + 2)
        break
    elif i == l - 2:
        continue
    elif s[i] == s[i + 2]:
        print(i + 1, i + 3)
        break
else:
    print(-1, -1)
