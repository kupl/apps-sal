from collections import deque
(n, k) = list(map(int, input().split()))
p = list(map(int, input().split()))
kitai = [0] * 1000
tmp = 0
for i in range(1000):
    tmp += i + 1
    kitai[i] = tmp / (i + 1)
total_kitai = [0] * (n + 1)
tmp = 0
for i in range(n):
    tmp += kitai[p[i] - 1]
    total_kitai[i + 1] = tmp
ans = 0
for i in range(n - k + 1):
    ans = max(total_kitai[i + k] - total_kitai[i], ans)
print(ans)
