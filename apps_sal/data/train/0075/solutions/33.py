import math

T = int(input())

for _ in range(T):
    N = int(input())
    v1 = complex(1, 0)
    angle = (N // 2) * (math.pi / N)
    v2 = complex(math.cos(angle), math.sin(angle))
    print(math.sqrt(2) * 0.5 * (abs(v1 + v2) + abs(v1 - v2)) * (1 / (2 * math.sin(math.pi / (2 * N)))))
