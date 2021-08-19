import math
(a, b) = map(str, input().split())
X = int(a) * 10 ** len(b) + int(b)
if math.sqrt(X) % 1 == 0:
    print('Yes')
else:
    print('No')
