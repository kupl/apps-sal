__author__ = 'asmn'
s = input()
pivot = s.find('^')
res = sum(map(lambda i_x: int(i_x[1]) * (i_x[0] - pivot) if i_x[1].isdigit() else 0, enumerate(s)))
print('left' if res < 0 else 'right' if res > 0 else 'balance')
