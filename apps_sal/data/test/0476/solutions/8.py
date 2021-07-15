import sys
str = input()

for i in range(0, len(str)):
    if str[i] == '1':
        continue
    elif str[i] == '4':
        if i > 0 and str[i - 1] == '1':
            continue
        elif i > 1 and str[i - 1] == '4' and str[i - 2] == '1':
            continue
        else:
            print('NO')
            return
    else:
        print('NO')
        return
        
print('YES')

