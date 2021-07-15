n = int(input())
s = input()

haszero = 0
for x in s:
    if(x=='0'):
        haszero = 1

hasup = 0
hasleft = 0
hasright = 0
hasdown = 0

for x in s:
    if(x=='1')or(x=='2')or(x=='3'):
        hasup = 1
    if(x=='1')or(x=='4')or(x=='7'):
        hasleft = 1
    if(x=='3')or(x=='6')or(x=='9'):
        hasright = 1
    if(x=='7')or(x=='0')or(x=='9'):
        hasdown = 1

if hasup and hasleft and hasright and hasdown:
    print('YES')
else:
    if hasup and haszero:
        print('YES')
    else:
        print('NO')
