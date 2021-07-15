X = int(input())
from itertools import count
for t in count(1,1):
    if (t-1)*t >= 2*(X-t):
        print(t); break
