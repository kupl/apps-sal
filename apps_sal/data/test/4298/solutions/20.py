N, D = map(int, input().split())

import numpy as np
print(int(np.ceil(N / (2*D + 1))))
