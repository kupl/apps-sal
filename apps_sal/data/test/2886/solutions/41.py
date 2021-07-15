import sys

s = input()

if len(s) == 2 and s[0] == s[1]:
    print('1 2')
    return
else:
    for i in range(0, len(s)-2):
        c1, c2, c3 = s[i], s[i+1], s[i+2]

        if len(set([c1,c2,c3])) <= 2:
                print(('%s %s' % (i+1, i+3)))
                return

print('-1 -1')

