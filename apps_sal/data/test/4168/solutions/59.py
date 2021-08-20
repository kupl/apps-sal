N = int(input())
s = ''
i = 0
while N != 0:
    if N % 2 == 0:
        s += '0'
        N //= 2
    else:
        s += '1'
        if i % 2 == 0:
            N = (N - 1) // 2
        else:
            N = (N + 1) // 2
    i += 1
if s == '':
    print('0')
else:
    print(s[::-1])
