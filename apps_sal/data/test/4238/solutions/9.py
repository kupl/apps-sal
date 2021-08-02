n = input()
num = 0
for i in n:
    num += int(i)
if num % 9 == 0:
    print('Yes')
else:
    print('No')
