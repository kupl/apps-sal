s = input()
l1 = list(input().split())
flag = 0
for item in l1:
    if item[0] == s[0]:
        flag = 1
        break
    elif item[1] == s[1]:
        flag = 1
        break
if flag == 1:
    print("YES")
else:
    print("NO")
