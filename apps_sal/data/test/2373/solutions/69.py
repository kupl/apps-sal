import math
n = int(input())
P = list(map(int, input().split()))

same = 0
cnt = 0
for i in range(n):
    if P[i] == i+1:
        same += 1
    else:
        cnt += math.ceil(same/2)
        same = 0

if same > 0:
    cnt += math.ceil(same/2)

print(cnt)
