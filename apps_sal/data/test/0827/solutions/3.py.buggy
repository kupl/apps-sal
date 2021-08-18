import math

n = int(input())
t = str(input())

len_t = len(t)

len_s = math.ceil(len_t / 3)

if t == '1':
    print(((10**10) * 2))
    return

s = ''

for i in range(len_s):
    s += '110'

if t not in s:
    len_s += 1
    s += '110'

if t in s:
    s.find('110')
    print((10**10 - len_s + 1))
else:
    print((0))
