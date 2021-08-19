import string
from collections import deque
number = int(input())
q = (number - 1) // 26
r = number % 26
sss = deque()
while True:
    sss.appendleft(string.ascii_lowercase[r - 1])
    if q == 0:
        break
    else:
        r = q % 26
        q = (q - 1) // 26
print(''.join(list(sss)))
