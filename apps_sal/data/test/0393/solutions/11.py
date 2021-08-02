n = int(input())
s = input()

if(len(s) == 1):
    if(s[0] == '1'):
        print('Yes')
    else:
        print('No')
else:
    if('000' in s or s[0] + s[1] == '00' or s[-1] + s[-2] == '00' or '11' in s):
        print('No')
    else:
        print('Yes')
