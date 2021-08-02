from math import *

s = input()
pos = [1]
for i in range(len(s)):
    c = s[i]
    if c == 'm' or c == 'w':
        pos[-1] = 0
        break
    if c == 'u' and i > 0 and s[i - 1] == 'u':
        pos.append(pos[-1] + pos[-2])
    elif c == 'n' and i > 0 and s[i - 1] == 'n':
        pos.append(pos[-1] + pos[-2])
    else:
        pos.append(pos[-1])
    pos[-1] %= 1000000007
print(pos[-1])
