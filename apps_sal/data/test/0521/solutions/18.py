n = int(input())
s = input()
flag = 0
for i in range(n - 1):
    if s[i] == '?':
        if s[i - 1] == s[i + 1]:
            flag = 1
            break
        if s[i + 1] == '?':
            flag = 1
            break
if s[0] == '?' or s[n - 1] == '?':
    flag = 1
for i in range(n - 1):
    if s[i] != '?' and s[i + 1] == s[i]:
        flag = 0
        break
if flag == 1:
    print("Yes")
else:
    print("No")
