import math
x = int(input())

cnt = 0
while x > 0:
    cnt += 1
    x -= cnt
print(cnt)
