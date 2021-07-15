import sys
a = len(input()) - 2
b = len(input()) - 2
c = len(input()) - 2
d = len(input()) - 2
x = [0, 0, 0, 0]
if (a >= 2 * b and a >= 2 * c and a >= 2 * d )or (2 * a <= b and 2 * a <=  c and 2 * a <=  d):
    x[0] = 1
if (b >= 2 * a and b >= 2 * c and b >= 2 * d )or (2 * b <=a and 2 * b <=  c and 2 * b <=  d):
    x[1] = 1
if (c >= 2 * b and c >= 2 * a and c >= 2 * d )or (2 * c <= a and 2 * c <= b and 2 * c <=  d):
    x[2] = 1
if (d >= 2 * b and d >= 2 * c and d >= 2 * a )or (2 * d <= b and 2 * d <=  c and 2 * d <= a):
    x[3] = 1

if sum(x) == 1:
    if x[0] == 1:
        print('A')
    if x[1] == 1:
        print('B')
    if x[2] == 1:
        print('C')
    if x[3] == 1:
        print('D')
else:
    print('C')
    


