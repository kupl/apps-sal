import math

N, D = map(int, input().split())
cnt_p = 0
for i in range(N):
    X, Y = map(int, input().split())
    Di = math.sqrt(X**2 + Y**2)
    if Di <= D:
        cnt_p += 1
print(cnt_p)
