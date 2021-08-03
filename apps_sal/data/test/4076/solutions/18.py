import math

A, B, H, M = map(int, input().split())

h_theta = 2 * math.pi * (H + M / 60) / 12
m_theta = 2 * math.pi * M / 60

dx = A * math.cos(h_theta) - B * math.cos(m_theta)
dy = A * math.sin(h_theta) - B * math.sin(m_theta)

print(math.sqrt(dx**2 + dy**2))
