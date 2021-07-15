m, r = list(map(int, input().split()))

answer = 0
from math import sqrt


def fef(vev):
    if vev == 0:
        return 0
    if vev <= 1:
        return 2 * r + sqrt(2) * r
    curr =  2 * r + sqrt(2) * r
    curr += (vev - 1) * (2 * r + sqrt(2)  *2 * r)

    curr += r * (vev - 1) * (vev - 2)
    return curr



for i in range(m):
    answer += fef(i)
    answer += fef(m - 1- i)
    answer += 2 * r

print(answer / (m ** 2))

