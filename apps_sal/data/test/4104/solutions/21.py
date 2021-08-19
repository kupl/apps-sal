import re
s = input()
print(eval(s) + eval(re.sub('-|\\+|\\d', lambda m: ['0', ['+3', '-5'][m[0] == '+']][m[0] in '+-'], s)))
