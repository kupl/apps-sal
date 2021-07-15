s = str(input())
s = s[::-1]

current = ""
answer = 0

for el in s:
    if '9' >= el >= '0':
        current += el
    elif el == '.':
        if len(current) == 2:
            current += '.'
    else:
        if current != '':
            answer += float(current[::-1])
            current = ''

temp = "%.2f" % answer
if temp[len(temp) - 2:] != '00':
    temp_2 = temp[:len(temp) - 3][::-1]
    temp = temp[len(temp) - 2:]
    parts = []
    current = ""
    for i in range(len(temp_2)):
        current += temp_2[i]
        if len(current) == 3:
            parts.append(current[::-1])
            current = ''
    if current != '':
        parts.append(current[::-1])
    print(*parts[::-1], sep='.', end='.')
    print(temp)

else:
    temp_2 = str(int(answer))[::-1]
    parts = []
    current = ""
    for i in range(len(temp_2)):
        current += temp_2[i]
        if len(current) == 3:
            parts.append(current[::-1])
            current = ''
    if current != '':
        parts.append(current[::-1])
    print(*parts[::-1], sep='.')
