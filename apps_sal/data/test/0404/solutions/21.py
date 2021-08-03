from math import sqrt, ceil

b = int(input())
cnt = 0

for j in range(1, int(sqrt(b)) + 1):
    if b % j == 0:
        cnt += 1
        d = b // j
        if j != d:
            cnt += 1

print(cnt)
