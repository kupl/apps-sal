from re import sub as b
print(eval(b('`', '-', b('(?P<a>-\\d*)', lambda x: b('-', '+3', x.group('a') * 3, 1), b('(?P<a>\\+\\d*)', lambda x: b('\\+', '`5', x.group('a') * 3, 1), input())))))
