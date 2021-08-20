from fileinput import *
for line in input():
    if lineno() == 1:
        n = int(line.strip())
if n % 2 == 0:
    li = [i + 1 for i in range(n)]
    (li[::2], li[1::2]) = (li[1::2], li[::2])
    print(''.join([str(num) + ' ' for num in li]))
else:
    print('-1')
