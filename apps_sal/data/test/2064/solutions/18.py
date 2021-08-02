n = int(input())

line = ''
if n % 2 == 0:
    one_num = int(n / 2)
    seven_num = 0
else:
    one_num = int(n / 2) - 1
    seven_num = 1

for i in range(seven_num):
    line += '7'

for i in range(one_num):
    line += '1'

print(line)
