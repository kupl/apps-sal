k = input()
import sys
Min = sys.maxsize
if '5' in k and '0' in k:
    temp = (len(k)-2) - k.rfind('5') + (len(k)-1) - k.rfind('0') 
    if (k.rfind('5') > k.rfind('0')):
        add = 0
        i = 1
        while k[i] == '0':
            add += 1
            i += 1
        temp += add
    if (temp<Min):
        Min = temp
if '2' in k and '5' in k:
    temp = (len(k)-2) - k.rfind('2') + (len(k)-1) - k.rfind('5') 
    if k.rfind('5')==0 and k[1]=='0' and len(k)>3:
        add = 0
        i = 1
        while k[i] == '0':
            add += 1
            i += 1
        temp += add
    if (k.rfind('2') > k.rfind('5')):
        temp += 1
    if (temp<Min):
        Min = temp
if '7' in k and '5' in k:
    temp = (len(k)-2) - k.rfind('7') + (len(k)-1) - k.rfind('5') 
    if k.rfind('5')==0 and k[1]=='0' and len(k)>3:
        add = 0
        i = 1
        while k[i] == '0':
            add += 1
            i += 1
        temp += add
    if (k.rfind('7') > k.rfind('5')):
        temp += 1
    if (temp<Min):
        Min = temp
if k.count('0')>1:
    css = k.rfind('0')
    temp = (len(k)-1) - css
    k = k[:css] + k[css+1:] 
    temp += (len(k)-1) - k.rfind('0') 
    if (temp<Min):
        Min = temp
if Min==sys.maxsize:
    print(-1)
else:
    print(Min)
