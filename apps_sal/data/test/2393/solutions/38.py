t =  int(input())

for i in range(t):
    stroka = 'cc' + input() + 'cc'
    s = list(stroka)
    r = 0
    indexes = []
    for j in range(len(s)):
        if s[j] == 'o':
            if (s[j+1] == 'n' and s[j+2] == 'e'):
                if s[j-1] == 'o':
                    indexes.append(j)
                else:
                    indexes.append(j-1)
                r+=1
            elif (s[j-1] == 'w' and s[j-2] == 't'):
                if s[j+1] == 'o':
                    indexes.append(j-2)
                else:
                    indexes.append(j-1)
                r+=1

    print(r)
    print(*indexes)

