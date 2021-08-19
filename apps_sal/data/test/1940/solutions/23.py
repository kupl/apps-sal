import math
(n, k) = list(map(int, input().split()))
line = list(map(int, input().split()))
cnt = 0
for x in line:
    cnt += math.ceil(x / k)
print(math.ceil(cnt / 2))
