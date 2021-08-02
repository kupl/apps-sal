from re import sub as b
print(eval(b(r'`', '-', b(r'(?P<a>-\d*)', lambda x: b('-', '+3', x.group('a') * 3, 1), b(r'(?P<a>\+\d*)', lambda x: b('\+', '`5', x.group('a') * 3, 1), input())))))
