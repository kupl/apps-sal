n = int(input())
a = 0
b = 0
s = input()
for i in range(n):
    if s[i] == '1':
        a += 1
    else:
        b += 1
if s == '0':
    print('0')
else:
    print('1' + '0' * b)
