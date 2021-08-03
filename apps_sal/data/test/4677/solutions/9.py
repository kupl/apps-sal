buf = ''
str = input()
for i in range(len(str)):
    if str[i] == 'B':
        if len(buf) != 0:
            buf = buf[0:len(buf) - 1]
        else:
            continue
    else:
        buf += str[i]

print(buf)
