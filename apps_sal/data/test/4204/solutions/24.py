s = input()
k = input()

for i in range(len(s)):
    if s[i] != '1':
        if int(k) <= i:
            print('1')
            break
        else:
            print(s[i])
            break
    else:
        if i == len(s) - 1:
            print('1')
