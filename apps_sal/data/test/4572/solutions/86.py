import re
s = str(input())
l = list('abcdefghijklmnopqrstuvwxyz')

for i in l:
    if not re.search(i,s):
        print(i)
        break
else:
    print('None')
