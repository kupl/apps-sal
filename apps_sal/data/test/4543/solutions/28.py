N = int(input().replace(' ', ''))
flag = False
for i in range(1, 10000):
    if N == i ** 2:
        flag = True
        break
    if N < i ** 2:
        break
if flag:
    print('Yes')
else:
    print('No')
