import re

S = input()
flag = True
while(flag):
    if(len(S)==0):
        flag = False
    if(S[-5:]=='dream' or S[-5:]=='erase'):
        S=S[:-5]
    elif(S[-6:]=='eraser'):
        S=S[:-6]
    elif(S[-7:]=='dreamer'):
        S=S[:-7]
    else:
        break
if(flag):
    print('NO')
else:
    print('YES')

