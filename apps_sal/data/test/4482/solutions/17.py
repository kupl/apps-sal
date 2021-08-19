import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)
N = int(input())
x = np.array(list(map(int, input().split())))
logging.debug('x={}'.format(x))
i = np.amin(x)
ans = []
while i <= np.amax(x):
    logging.debug('i={}'.format(i))
    y = np.array([i] * N)
    ans.append(sum((x - y) ** 2))
    logging.debug('ans={}'.format(ans))
    i += 1
print(min(ans))
