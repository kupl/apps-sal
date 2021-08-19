a = input()
b = 0
for i in a:
    b += int(i)
if int(a) % b == 0:
    print('Yes')
else:
    print('No')
