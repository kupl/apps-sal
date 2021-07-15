s = input()
t = input()
flg = 0
for i in range(len(s)):
    if t[i] != s[i]:
        flg = 1
        break
if flg:
    print("No")
else:
    print("Yes")
