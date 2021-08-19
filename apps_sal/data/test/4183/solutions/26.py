import numpy as np
with open(0) as f:
    (N, *T) = map(int, f.read().split())
ans = 1
for t in T:
    ans = np.lcm(ans, t)
print(ans)
