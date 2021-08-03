import numpy as np
h, w = map(int, input().split())
s = np.array([list(input()) for i in range(h)])
s = (s[np.any(s == '#', axis=1)])
s = (s[:, np.any(s == '#', axis=0)])
for i in s:
    print("".join(map(str, i)))
