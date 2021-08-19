a = input()
sum = 0
for i in a:
    sum = sum + ord(i) - 48
a = int(a)
if a % sum == 0:
    print('Yes')
else:
    print('No')
