a = input().strip()
st = ''
x = ''
mul = 0
t = 0
for i in a:
    if i in '1234567890':
        mul = mul * 10 + int(i)
    elif i == '-':
        st += x * mul
        x = ''
        t = 0
        mul = 0
    elif t == 1:
        x += i
    elif i == '+':
        t = 1
    else:
        st += i
if st == st[::-1]:
    print('Return')
else:
    print('Continue')
