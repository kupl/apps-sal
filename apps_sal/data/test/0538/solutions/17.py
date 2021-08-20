x = input()
for i in range(len(x)):
    count = len(x) - i - 1
    if x[len(x) - i - 1] != '0':
        break
x = x[:count + 1]
if x == x[::-1]:
    print('YES')
else:
    print('NO')
