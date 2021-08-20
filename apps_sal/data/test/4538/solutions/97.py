import math
(N, D) = map(int, input().split())
answer = 0
for i in range(N):
    (X, Y) = map(int, input().split())
    distance = math.sqrt(X ** 2 + Y ** 2)
    if distance <= D:
        answer += 1
print(answer)
