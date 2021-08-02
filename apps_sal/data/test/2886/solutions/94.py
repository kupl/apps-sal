s = input()
for i in range(len(s) - 2):
    if len(set(s[i:i + 3])) <= 2:
        print(i + 1, i + 3)
        break
else:
    if s[0] == s[1]:
        print(1, 2)
    else:
        print(-1, -1)
