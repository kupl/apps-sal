name = input()
stroka = input()
lengthName = len(name)
lengthStroka = len(stroka)
indexFirst = 0
indexLast = 0
for i in range(lengthName):
    j = 0
    while j + indexFirst != lengthStroka:
        if stroka[j + indexFirst] == name[i]:
            indexFirst = j + indexFirst + 1
            break
        j += 1
i = 0
stroka = stroka[::-1]
name = name[::-1]
for i in range(lengthName):
    j = 0
    while j + indexLast != lengthStroka:
        if stroka[j + indexLast] == name[i]:
            indexLast = j + indexLast + 1
            break
        j += 1
if lengthStroka - indexLast - indexFirst + 1 < 0:
    print(0)
else:
    print(lengthStroka - indexLast - indexFirst + 1)
