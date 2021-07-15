import sys

a = sys.stdin.readline().split()[0]
b = sys.stdin.readline().split()[0]
i, j = 0, 0
if (len(a) < len(b)):
    a = '0' * (len(b) - len(a)) + a
else:
    b = '0' * (len(a) - len(b)) + b
while (i < len(a)) and (j < len(b)) and (a[i] == b[j]):
    i += 1
    j += 1
if (i == len(a)) and (j == len(b)):
    print('=')
elif j == len(b):
    print('>')
elif i == len(a):
    print('<')
else:
    #print(')')
    print('<' if (a[i] < b[j]) else '>')
