import math
import numpy as np
a, b, h, m = list(map(int, input().split()))
a_radian = math.radians(h * 30 + m / 2)
a_ = np.array([a * math.cos(a_radian), a * math.sin(a_radian)])

b_radian = math.radians(6 * m)
b_ = np.array([b * math.cos(b_radian), b * math.sin(b_radian)])

print(np.linalg.norm(a_ - b_))
