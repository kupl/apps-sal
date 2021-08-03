s = str(input())
flag = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print(str(i + 1) + " " + str(i + 2))
        flag = 1
        break
if flag == 0:
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            print(str(i + 1) + " " + str(i + 3))
            flag = 1
            break
if flag == 0:
    print("-1 -1")
