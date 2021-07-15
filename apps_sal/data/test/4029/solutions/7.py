k = input()
n = len(k)
import sys
Min = sys.maxsize
ck = ['50','25','75']
for c in ck:
    if c[0] in k and c[1] in k:
        temp = 2*n - 3 - k.rfind(c[0]) - k.rfind(c[1]) 
        if (c[1]=='5'):
            if k.rfind('5')==0 and k[1]=='0' and n>3:
                add = 0
                i = 1
                while k[i] == '0':
                    add += 1
                    i += 1
                temp += add
        temp += k.rfind(c[0]) > k.rfind(c[1])
        Min = min(temp,Min)
if k.count('0')>1:
    css = k.rfind('0')
    temp = n-1 - css
    k = k[:css] + k[css+1:] 
    temp += len(k)-1 - k.rfind('0')
    Min = min(temp,Min)
print([Min,-1][Min==sys.maxsize])
