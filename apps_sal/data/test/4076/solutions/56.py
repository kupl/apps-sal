import numpy as np
(A, B, H, M) = map(int, input().split())
pi = np.pi
h_angle = (H + M / 60) * 2 * pi / 12
m_angle = M * 2 * pi / 60
h_x = A * np.cos(h_angle)
h_y = A * np.sin(h_angle)
m_x = B * np.cos(m_angle)
m_y = B * np.sin(m_angle)
print(np.sqrt((h_x - m_x) ** 2 + (h_y - m_y) ** 2))
