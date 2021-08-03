import operator
import functools
n = int(input())
a = input().split()
notpretty = 0

zero = False
for i in range(n):
    for j in range(len(a[i])):
        if (j == 0 and a[i][j] != '1') or (j != 0 and a[i][j] != '0'):
            #print(i, j, a[i][j])
            notpretty = i
        if (j == 0 and a[i][j] == '0'):
            zero = True
            break
l = 0
if zero:
    print(0)
else:
    for i in range(n):
        if i != notpretty:
            l += len(a[i]) - 1
    print(a[notpretty], '0' * l, sep='')
