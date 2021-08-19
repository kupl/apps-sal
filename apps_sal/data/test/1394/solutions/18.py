s = input()
notA = 0
lis = []
for i in s:
    if i != 'a':
        notA += 1
        lis.append(i)
if notA % 2 == 1:
    print(':(')
else:
    check = 1
    for i in range(notA // 2):
        if lis[i] != lis[notA // 2 + i]:
            print(':(')
            check = 0
            break
    for i in range(len(s) - 1, len(s) - 1 - notA // 2, -1):
        if s[i] == 'a':
            print(':(')
            check = 0
            break
    if check == 1:
        print(s[:len(s) - notA // 2])
