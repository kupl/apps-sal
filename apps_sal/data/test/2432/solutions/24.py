"""from math import sqrt, ceil
a = int(input())
for i in range(2, ceil(sqrt(a)) + 1):
    if a % i == 0:
        print(i, end='')
        print(a//i)
"""
a = int(input())
s = [1, 2, 4, 8, 16, 32]
s1 = ''
s2 = ''
for i in s[::-1]:
    if a - i >= 0:
        a -= i
        s1 += '1'
    else:
        s1 += '0'
s2 = s1[0]
s2 += s1[5]
s2 += s1[3]
s2 += s1[2]
s2 += s1[4]
s2 += s1[1]
b = 0
for i in range(6):
    b += int(s2[5 - i]) * s[i]
print(b)
