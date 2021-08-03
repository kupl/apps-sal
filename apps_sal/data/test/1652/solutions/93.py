s = input()
s = s[::-1]
lis = ['remaerd', 'resare', 'esare', 'maerd']
i = 0
j = 0
#s = s[::-1]
while i < len(s):
    tmp = ''
    while j < len(s):
        tmp += s[j]
        # print(tmp)
        if len(tmp) == 8:
            print('NO')
            return
        elif tmp in lis:
            i = j + 1
            j = i
            break
        else:
            j += 1
print('YES')
