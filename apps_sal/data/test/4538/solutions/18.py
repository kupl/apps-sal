import math
(N, D) = map(int, input().split())
cnt = 0
for i in range(N):
    (x, y) = map(int, input().split())
    ans = math.sqrt(x ** 2 + y ** 2)
    if ans <= D:
        cnt += 1
print(cnt)
