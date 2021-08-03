s = list(input())
a = ['*']
d = 0
for i in range(len(s)):
    if s[i] == a[-1]:
        a.pop()
        d += 1
    else:
        a.append(s[i])
if d % 2 == 1:
    print("Yes")
else:
    print("No")
