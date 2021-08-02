s = input()

flag = True
for i in range(len(s) - 1):
    if s[i + 1] == s[i]:
        flag = False
print(("Good" if flag else "Bad"))
