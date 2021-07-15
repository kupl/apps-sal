n = int(input())
a = list(str(n))
b = 0
for i in a:
    b += int(i)
if n % b == 0:
    print('Yes')
else:
    print('No')
