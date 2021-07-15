import math

is_no = 0
num1, num2 = list(map(int, input().split()))
str1 = input()
table = list(str1)
count = 0
for i in range(len(str1)):
    if table[i] == '-':
        count += 1
    else:
        continue
if count == 1 and table[num1] =='-':
    print('Yes')
else:
    print('No')

