a = input()
b = ''
for i in range(len(a)):
    b += a[len(a) - i - 1]
if a == b:
    print('Yes')
else:
    print('No')
