s = input().split('"')
for i in range(len(s)):
    if i % 2:
        print('<', s[i], '>', sep='')
    else:
        l = [x for x in s[i].split() if x != '']
        if l != []:
            print('<', '>\n<'.join(l), '>', sep='')
