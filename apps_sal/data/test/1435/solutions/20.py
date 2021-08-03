s = input()
nine = []
num = 0
ans = 1
for i in range(1, len(s)):
    if int(s[i - 1]) + int(s[i]) == 9:
        num += 1
    else:
        if num > 0:
            nine.append(num + 1)
            num = 0
if num != 0:
    nine.append(num + 1)
for i in range(len(nine)):
    x = nine[i]
    if x % 2 != 0:
        ans = ans * (int((x + 1) / 2))
print(ans)
