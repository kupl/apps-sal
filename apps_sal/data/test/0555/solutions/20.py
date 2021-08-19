a = input('')
counter = 0
strN = ''
for i in a:
    num = int(i)
    if counter == 0:
        if num == 9 or 9 - num > num:
            strN = strN + i
        else:
            strN = strN + str(9 - num)
    elif 9 - num > num:
        strN = strN + i
    else:
        strN = strN + str(9 - num)
    counter = counter + 1
print(int(strN))
