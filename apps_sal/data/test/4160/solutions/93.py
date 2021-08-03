import math
X = int(input())

ret = 100
cnt = 0
while ret < X:
    ret += ret // 100
    cnt += 1

print(cnt)
