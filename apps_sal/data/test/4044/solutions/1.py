(a, b, x) = list(map(int, input().split()))
n = a + b

if a > b:
    s = '0'
    a -= 1
else:
    s = '1'
    b -= 1

for i in range(1, n):
    if x > 1:
        if s[i - 1] == '0':
            s = s + '1'
            b -= 1
        else:
            s = s + '0'
            a -= 1
        x -= 1
    elif s[i - 1] == '0':
        if a > 0:
            s = s + '0'
            a -= 1
        else:
            s = s + '1'
            b -= 1
    else:
        if b > 0:
            s = s + '1'
            b -= 1
        else:
            s = s + '0'
            a -= 1

print(s)

