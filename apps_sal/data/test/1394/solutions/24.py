s = input()
l1 = []
for c in s:
    if c != 'a':
        l1.append(c)
if len(l1) % 2 == 0:
    flag = 0

    for i in range(0, len(l1) // 2):
        if l1[i] == l1[len(l1) // 2 + i]:
            continue
        else:
            flag = 1
            break
    if flag == 1:
        print(":(")
    else:
        flag = 0
        for c in s[len(s) - len(l1) // 2:]:
            if c == 'a':
                flag = 1
                break
        if flag == 0:

            print(s[:len(s) - len(l1) // 2])
        else:
            print(":(")
else:
    print(":(")
