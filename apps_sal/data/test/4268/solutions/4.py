import math


def calc_distance(Y, Z):
    temp = 0
    for y, z in zip(Y, Z):
        temp += (y - z)**2
    return temp


def is_integer(num):
    for k in range(1, num + 1):
        if k * k == num:
            return True
    else:
        return False


N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(len(X) - 1):
    for j in range(i, len(X)):
        distance = calc_distance(X[i], X[j])
        if is_integer(distance):
            cnt += 1
print(cnt)
