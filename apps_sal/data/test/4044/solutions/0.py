
a, b, x = list(map(int, input().split()))
if(a > b):
    s = '0'
    a -= 1
else:
    s = '1'
    b -= 1
for i in range(x - 1):
    if(s[-1] == '1'):
        s += '0'
        a -= 1
    else:
        s += '1'
        b -= 1
if(s[-1] == '1'):
    s += '1' * (b)
    s += '0' * a
else:
    s += '0' * a
    s += '1' * b
print(s)
