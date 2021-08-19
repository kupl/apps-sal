word = input()
flag = False
C_count = 0
if word[0] == 'A':
    for i in range(2, len(word) - 1):
        if word[i] == 'C' and C_count == 0:
            C_count += 1
            C_place = i
        elif word[i] == 'C' and C_count == 1:
            C_count += 1
    if C_count == 1:
        for i in range(1, len(word)):
            if word[i].isupper() and i != C_place:
                break
            if i == len(word) - 1:
                flag = True
if flag:
    print('AC')
else:
    print('WA')
