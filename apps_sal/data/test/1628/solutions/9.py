__author__ = 'runekri3'
s = input()
x_count = s.count('x')
y_count = s.count('y')
if x_count > y_count:
    char = 'x'
else:
    char = 'y'
print(char * abs(x_count - y_count))
