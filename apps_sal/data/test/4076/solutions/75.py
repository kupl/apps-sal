import math
import numpy as np


def rot_rev(t, v):
    R = np.array([[np.cos(t), np.sin(t)], [-np.sin(t), np.cos(t)]])
    return np.dot(R, v)


(A, B, H, M) = list(map(int, input().split()))
H_rad = (H * 60 + M) / (12 * 60) * 2 * np.pi
M_rad = M / 60 * 2 * np.pi
P_A = (0, A)
P_B = (0, B)
rot_A = rot_rev(H_rad, P_A)
rot_B = rot_rev(M_rad, P_B)
print(np.linalg.norm(rot_A - rot_B))
