s = input().split(' ')
n = int(s[0])
a = int(s[1])
b = int(s[2])
if n > a * b:
    print(-1)
else:
    for i in range(a):
        s = ''
        for j in range(b):
            if i % 2 == 0:
                m = i * b + j + 1
                if m <= n:
                    s += str(m) + ' '
                else:
                    s += '0 '
            else:
                m = (i + 1) * b - j
                if m <= n:
                    s += str(m) + ' '
                else:
                    s += '0 '
        print(s)
