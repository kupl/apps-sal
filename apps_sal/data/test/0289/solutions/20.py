import sys
import math
s = input()
cnt = s.count('VK')
if s[:2] == 'KK':
    cnt += 1
elif s[-2:] == 'VV':
    cnt += 1
elif s.find('VVV') >= 0:
    cnt += 1
elif s.find('KKK') >= 0:
    cnt += 1
print(cnt)
